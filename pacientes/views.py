from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .forms import *
from .utils import to_json
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class PacienteView(APIView):
    def get(self, request, paciente_id, format=None):
        try:
            paciente = Paciente.objects.get(id=paciente_id)
        except Paciente.DoesNotExist:
            response = Response({'error': 'Ese paciente no existe'}, status=status.HTTP_404_NOT_FOUND)

        pac_json = PacienteSerializer(paciente).data
        hosp_json = HospitalSerializer(paciente.hospitales.all(), many=True).data
        hist_json = HistoriaSerializer(Historia.objects.filter(paciente=paciente), many=True).data

        pac_json['hospitales'] = hosp_json
        pac_json['historia'] = hist_json

        return Response(pac_json, status=status.HTTP_200_OK)


class PacientePermisoHospitalView(APIView):
    def get_objects(self, paciente_id, hospital_id):
        try:
            paciente = Paciente.objects.get(id=paciente_id)
        except Paciente.DoesNotExist:
            response = Response({'error': 'Ese paciente no existe'}, status=status.HTTP_404_NOT_FOUND)
            return [response, None, None]

        try:
            hospital = Hospital.objects.get(id=hospital_id)
        except Hospital.DoesNotExist:
            response = Response({'error': 'Ese hospital no existe'}, status=status.HTTP_404_NOT_FOUND)
            return [response, None, None]

        return [None, paciente, hospital]

    def post(self, request, paciente_id, hospital_id, format=None):
        error, paciente, hospital = self.get_objects(paciente_id, hospital_id)
        if error:
            return error

        paciente.hospitales.add(hospital)
        return Response({'mensaje': 'Se dio permiso al hospital'}, status=status.HTTP_200_OK)

    def delete(self, request, paciente_id, hospital_id, format=None):
        error, paciente, hospital = self.get_objects(paciente_id, hospital_id)
        if error:
            return error

        paciente.hospitales.remove(hospital)
        return Response({'mensaje': 'Se removio el permiso al hospital'}, status=status.HTTP_200_OK)


class PacientePorCurpView(APIView):
    def get(self, request, curp):
        try:
            paciente = Paciente.objects.get(curp=curp)
        except Paciente.DoesNotExist:
            response = Response({'error': 'Ese paciente no existe'}, status=status.HTTP_404_NOT_FOUND)

        return Response({'id': paciente.id}, status=status.HTTP_200_OK)


# obtiene el paciente solo si el hospital tiene permisos
class PacienteTieneHospitalView(APIView):
    def get(self, request, curp, hospital_id):
        try:
            paciente = Paciente.objects.get(curp=curp)
        except Paciente.DoesNotExist:
            return Response({'error': 'Ese paciente no existe'}, status=status.HTTP_404_NOT_FOUND)

        try:
            hospital = paciente.hospitales.get(id=hospital_id)
        except Hospital.DoesNotExist:
            return Response({'error': 'Ese hospital no tiene permisos'}, status=status.HTTP_200_OK)

        return Response({'id': paciente.id}, status=status.HTTP_200_OK)


class EventosView(APIView):
    def get(self, request, paciente_id):
        eventos = Evento.objects.filter(paciente=paciente_id)

        if not eventos:
            return JsonResponse({'warning': 'Paciente sin eventos'}, status=status.HTTP_204_NO_CONTENT)

        eventos_json = EventoSerializer(eventos, many=True).data

        for evento_json in eventos_json:
            # tomas
            tomas_json = TomaSerializer(Toma.objects.filter(evento=evento_json['id']), many=True).data
            for toma_json in tomas_json:
                signos = SignoVital.objects.filter(toma=toma_json['id'])
                signos_json = SignoVitalSerializer(signos, many=True).data
                toma_json['signos'] = signos_json
            evento_json['tomas'] = tomas_json

            # recetas
            recetas_json = RecetaSerializer(Receta.objects.filter(evento=evento_json['id']), many=True).data
            for receta_json in recetas_json:
                meds = Medicamento.objects.filter(receta=receta_json['id'])
                meds_json = MedicamentoSerializer(meds, many=True).data
                receta_json['medicamentos'] = meds_json
            evento_json['recetas'] = recetas_json

            # diagnosticos
            diags_json = DiagnosticoSerializer(Diagnostico.objects.filter(evento=evento_json['id']), many=True).data
            evento_json['diagnosticos'] = diags_json

            # intervenciones
            inter_json = IntervencionSerializer(Intervencion.objects.filter(evento=evento_json['id']), many=True).data
            evento_json['intervenciones'] = inter_json

        return Response(eventos_json, status=status.HTTP_200_OK)


class HistoriaView(APIView):
    def get(self, request, paciente_id):
        historial = Historia.objects.filter(paciente=paciente_id)

        if not historial:
            return JsonResponse({'warning': 'Paciente sin historia'}, status=status.HTTP_204_NO_CONTENT)

        hist_json = HistoriaSerializer(historial, many=True).data
        return Response(hist_json, status=status.HTTP_200_OK)


class AlergiasView(APIView):
    def get(self, request, paciente_id):
        alergias = Alergia.objects.filter(paciente=paciente_id)

        if not alergias:
            return Response({'warning': 'Paciente sin alergias'}, status=status.HTTP_204_NO_CONTENT)

        aler_json = AlergiaSerializer(alergias, many=True).data
        return Response(aler_json, status=status.HTTP_200_OK)

    def post(self, request, paciente_id):
        serializer = AlergiaSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DiagnosticosView(APIView):
    def get(self, request, paciente_id):
        diags = Diagnostico.objects.filter(paciente=paciente_id)

        if not diags:
            return JsonResponse({'warning': 'Paciente sin diagnosticos'}, status=status.HTTP_204_NO_CONTENT)

        diag_json = DiagnosticoSerializer(diags, many=True).data
        return Response(diag_json, status=status.HTTP_200_OK)


class IntervencionesView(APIView):
    def get(self, request, paciente_id):
        intervenciones = Intervencion.objects.filter(paciente=paciente_id)

        if not intervenciones:
            return JsonResponse({'warning': 'Paciente sin intervenciones'}, status=status.HTTP_204_NO_CONTENT)

        inter_json = IntervencionSerializer(intervenciones, many=True).data
        return Response(inter_json, status=status.HTTP_200_OK)


class MedicamentosView(APIView):
    def get(self, request, paciente_id):
        medicamentos = Medicamento.objects.filter(paciente=paciente_id)

        if not medicamentos:
            return JsonResponse({'warning': 'Paciente sin medicamentos'}, status=status.HTTP_204_NO_CONTENT)

        meds_json = MedicamentoSerializer(medicamentos, many=True).data
        return Response(meds_json, status=status.HTTP_200_OK)

    def post(self, request, paciente_id):
        serializer = MedicamentoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TomasSignosView(APIView):
    def get(self, request, paciente_id):
        tomas = Toma.objects.filter(paciente=paciente_id)

        if not tomas:
            return JsonResponse({'warning': 'Paciente sin tomas de signos vitales'}, status=status.HTTP_204_NO_CONTENT)

        tomas_json = to_json(tomas, True)

        for toma_json in tomas_json:
            signos = SignoVital.objects.filter(toma=toma_json['id'])
            signos_json = to_json(signos, True)
            toma_json['signos'] = signos_json

        return Response(tomas_json, status=status.HTTP_200_OK)


class RecetasView(APIView):
    def get(self, request, paciente_id):
        recetas = Receta.objects.filter(paciente=paciente_id)

        if not recetas:
            return Response({'warning': 'Paciente sin recetas'}, status=status.HTTP_204_NO_CONTENT)

        recetas_json = RecetaSerializer(recetas, many=True).data

        for receta_json in recetas_json:
            meds = Medicamento.objects.filter(receta=receta_json['id'])
            meds_json = MedicamentoSerializer(meds, many=True).data
            receta_json['medicamentos'] = meds_json

        return Response(recetas_json, status=status.HTTP_200_OK)
