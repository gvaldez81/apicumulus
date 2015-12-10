from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .models import *
from .serializers import *
from .utils import raw_sql_search, secret_key_gen
from .permissions import PacienteView, isApp, AppView

# Create your views here.
@api_view(['GET'])
def routes(request, format=None):
    routes = [
        '/search/',
        '/pacientes/<curp>/',
        '/pacientes/<curp>/hospital/<hospital_id>/',
        '/pacientes/<paciente_id>/',
        '/pacientes/<paciente_id>/alergias',
        '/pacientes/<paciente_id>/diagnosticos',
        '/pacientes/<paciente_id>/eventos',
        '/pacientes/<paciente_id>/cuestionarios',
        '/pacientes/<paciente_id>/hospital/<hospital_id>/',
        '/pacientes/<paciente_id>/intervenciones',
        '/pacientes/<paciente_id>/medicamentos',
        '/pacientes/<paciente_id>/recetas',
        '/pacientes/<paciente_id>/tomas_signos',
    ]

    return Response({'routes': routes}, status=status.HTTP_200_OK)

@api_view(['POST'])
def search(request, format=None):
    query = request.POST.get('query','')

    if not query:
        return Response({'error:' 'Missing query parameter'}, status=status.HTTP_400_BAD_REQUEST)

    result = raw_sql_search(query)

    return Response(result, status=status.HTTP_200_OK)

@api_view(['GET','POST'])
def login(request, format=None):
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')

        if not username or not password:
            return Response({'message': 'Incorrect params'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)
        if not user:
            return Response({'message': 'No such user'}, status=status.HTTP_404_NOT_FOUND)
    else:
        if request.user.is_authenticated():
            user = request.user
        else:
            return Response({'message': 'No params'}, status=status.HTTP_400_BAD_REQUEST)

    token, created = Token.objects.get_or_create(user=user)

    return Response({'token': token.key}, status=status.HTTP_200_OK)

@api_view(['POST'])
def apptoken(request, format=None):
    username = request.POST.get('username','')
    password = request.POST.get('password','')

    if not username or not password:
        return Response({'message': 'Incorrect params'}, status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(username=username, password=password)
    if not user:
        return Response({'message': 'No such user'}, status=status.HTTP_404_NOT_FOUND)

    if isApp(user):
        return login(request)
    else:
        return Response({'message': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)

class AppResetKeyView(AppView):
    def post(self, request, format=None):
        key = secret_key_gen()
        request.user.set_password(key)
        request.user.save()
        print key
        return Response({'key':key},status=status.HTTP_205_RESET_CONTENT)

class PacienteDetailView(PacienteView):
    def get(self, request, paciente_id, format=None):
        paciente = self.get_ctapac(paciente_id)

        pac_json = PacienteSerializer(paciente).data
        hosp_json = HospitalSerializer(paciente.hospitales.all(), many=True).data

        pac_json['hospitales'] = hosp_json

        return Response(pac_json, status=status.HTTP_200_OK)

class PacientePermisoHospitalView(PacienteView):
    def get_objects(self, paciente_id, hospital_id):
        paciente = self.get_ctapac(paciente_id)

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

class PacientePorCurpView(PacienteView):
    def get(self, request, curp, format=None):
        paciente = self.get_ctapac(paciente_id)

        return Response({'id': paciente.id}, status=status.HTTP_200_OK)

# obtiene el paciente solo si el hospital tiene permisos
class PacienteTieneHospitalView(PacienteView):
    def get(self, request, curp, hospital_id, format=None):
        paciente = self.get_ctapac(paciente_id)

        try:
            hospital = paciente.hospitales.get(id=hospital_id)
        except Hospital.DoesNotExist:
            return Response({'error': 'Ese hospital no tiene permisos'}, status=status.HTTP_200_OK)

        return Response({'id': paciente.id}, status=status.HTTP_200_OK)

class EventosView(PacienteView):
    def get(self, request, paciente_id, format=None):
        paciente = self.get_ctapac(paciente_id)
        eventos = Evento.objects.filter(paciente=paciente)

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

class CuestionarioView(PacienteView):
    def get(self, request, paciente_id, format=None):
        paciente = self.get_ctapac(paciente_id)
        cuestionario = Cuestionario.objects.filter(paciente=paciente)

        if not cuestionario:
            return JsonResponse({'warning': 'Paciente sin cuestionarios contestados'}, status=status.HTTP_204_NO_CONTENT)

        cuest_json = CuestionarioSerializer(cuestionario, many=True).data
        return Response(cuest_json, status=status.HTTP_200_OK)

class AlergiasView(PacienteView):
    def get(self, request, paciente_id, format=None):
        paciente = self.get_ctapac(paciente_id)
        alergias = Alergia.objects.filter(paciente=paciente)

        if not alergias:
            return Response({'warning': 'Paciente sin alergias'}, status=status.HTTP_204_NO_CONTENT)

        aler_json = AlergiaSerializer(alergias, many=True).data
        return Response(aler_json, status=status.HTTP_200_OK)

    def post(self, request, paciente_id, format=None):
        self.get_ctapac(paciente_id)
        serializer = AlergiaSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DiagnosticosView(PacienteView):
    def get(self, request, paciente_id, format=None):
        paciente = self.get_ctapac(paciente_id)
        diags = Diagnostico.objects.filter(paciente=paciente)

        if not diags:
            return JsonResponse({'warning': 'Paciente sin diagnosticos'}, status=status.HTTP_204_NO_CONTENT)

        diag_json = DiagnosticoSerializer(diags, many=True).data
        return Response(diag_json, status=status.HTTP_200_OK)

class IntervencionesView(PacienteView):
    def get(self, request, paciente_id, format=None):
        paciente = self.get_ctapac(paciente_id)
        intervenciones = Intervencion.objects.filter(paciente=paciente)

        if not intervenciones:
            return JsonResponse({'warning': 'Paciente sin intervenciones'}, status=status.HTTP_204_NO_CONTENT)

        inter_json = IntervencionSerializer(intervenciones, many=True).data
        return Response(inter_json, status=status.HTTP_200_OK)

class MedicamentosView(PacienteView):
    def get(self, request, paciente_id, format=None):
        paciente = self.get_ctapac(paciente_id)
        medicamentos = Medicamento.objects.filter(paciente=paciente)

        if not medicamentos:
            return JsonResponse({'warning': 'Paciente sin medicamentos'}, status=status.HTTP_204_NO_CONTENT)

        meds_json = MedicamentoSerializer(medicamentos, many=True).data
        return Response(meds_json, status=status.HTTP_200_OK)

    def post(self, request, paciente_id, format=None):
        paciente = self.get_ctapac(paciente_id)
        serializer = MedicamentoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TomasSignosView(PacienteView):
    def get(self, request, paciente_id, format=None):
        paciente = self.get_ctapac(paciente_id)
        tomas = Toma.objects.filter(paciente=paciente)

        if not tomas:
            return JsonResponse({'warning': 'Paciente sin tomas de signos vitales'}, status=status.HTTP_204_NO_CONTENT)

        tomas_json = TomaSerializer(tomas, many=True).data

        for toma_json in tomas_json:
            signos = SignoVital.objects.filter(toma=toma_json['id'])
            signos_json = SignoVitalSerializer(signos, many=True).data
            toma_json['signos'] = signos_json

        return Response(tomas_json, status=status.HTTP_200_OK)

class RecetasView(PacienteView):
    def get(self, request, paciente_id, format=None):
        paciente = self.get_ctapac(paciente_id)
        recetas = Receta.objects.filter(paciente=paciente)

        if not recetas:
            return Response({'warning': 'Paciente sin recetas'}, status=status.HTTP_204_NO_CONTENT)

        recetas_json = RecetaSerializer(recetas, many=True).data

        for receta_json in recetas_json:
            meds = Medicamento.objects.filter(receta=receta_json['id'])
            meds_json = MedicamentoSerializer(meds, many=True).data
            receta_json['medicamentos'] = meds_json

        return Response(recetas_json, status=status.HTTP_200_OK)
