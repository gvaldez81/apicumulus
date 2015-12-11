from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from .models import *
from .serializers import *
from .utils import raw_sql_search, secret_key_gen
from .permissions import PacienteView, EventoView, isApp

# Create your views here.
@api_view(['GET'])
def routes(request, format=None):
    routes = [
        '/search/',
        '/pacientes/<curp>/',
        '/pacientes/<curp>/hospital/<hospital_id>/',
        '/pacientes/<curp>/',
        '/pacientes/<curp>/alergias',
        '/pacientes/<curp>/diagnosticos',
        '/pacientes/<curp>/eventos',
        '/pacientes/<curp>/cuestionarios',
        '/pacientes/<curp>/hospital/<hospital_id>/',
        '/pacientes/<curp>/intervenciones',
        '/pacientes/<curp>/medicamentos',
        '/pacientes/<curp>/recetas',
        '/pacientes/<curp>/tomas_signos',
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
        username = request.data.get('username','')
        password = request.data.get('password','')

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

class PacienteDetailView(PacienteView):
    def get(self, request, curp, format=None):
        paciente = self.get_pac(curp)

        pac_json = PacienteSerializer(paciente).data
        # hosp_json = HospitalSerializer(paciente.hospitales.all(), many=True).data
        # pac_json['hospitales'] = hosp_json

        return Response(pac_json, status=status.HTTP_200_OK)

    # def put(self, request, c)


# Relacionado a eventos
# Lista de Eventos
class EventosView(PacienteView):
    def get(self, request, curp, format=None):
        paciente = self.get_pac(curp)
        eventos = Evento.objects.filter(paciente=paciente)

        if not eventos:
            return JsonResponse({'warning': 'Paciente sin eventos'}, status=status.HTTP_204_NO_CONTENT)

        eventos_json = EventoSerializer(eventos, many=True).data

        return Response(eventos_json, status=status.HTTP_200_OK)

# Detalles del evento
class EventoDetailView(EventoView):
    def get(self, request, curp, evento_id, format=None):
        paciente = self.get_pac(curp)
        evento = self.get_evento(evento_id)

        evento_json = EventoSerializer(evento).data

        # tomas
        tomas_json = TomaSerializer(Toma.objects.filter(evento=evento), many=True).data
        for toma_json in tomas_json:
            signos = SignoVital.objects.filter(toma=toma_json['id'])
            signos_json = SignoVitalSerializer(signos, many=True).data
            toma_json['signos'] = signos_json
        evento_json['tomas'] = tomas_json

        # recetas
        recetas_json = RecetaSerializer(Receta.objects.filter(evento=evento), many=True).data
        for receta_json in recetas_json:
            meds = Medicamento.objects.filter(receta=receta_json['id'])
            meds_json = MedicamentoSerializer(meds, many=True).data
            receta_json['medicamentos'] = meds_json
        evento_json['recetas'] = recetas_json

        # diagnosticos
        diags_json = DiagnosticoSerializer(Diagnostico.objects.filter(evento=evento), many=True).data
        evento_json['diagnosticos'] = diags_json

        # intervenciones
        inter_json = IntervencionSerializer(Intervencion.objects.filter(evento=evento), many=True).data
        evento_json['intervenciones'] = inter_json

        # cuestionarios
        cuest_json = CuestionarioSerializer(Cuestionario.objects.filter(evento=evento), many=True).data
        evento_json['cuestionarios'] = cuest_json

        return Response(evento_json, status=status.HTTP_200_OK)

# Diagnosticos del evento
class DiagnosticosView(EventoView):
    def get(self, request, curp, evento_id, format=None):
        paciente = self.get_pac(curp)
        evento = self.get_evento(evento_id)
        diags = Diagnostico.objects.filter(paciente=paciente, evento=evento)

        if not diags:
            return Response({'warning': 'Paciente sin diagnosticos'}, status=status.HTTP_204_NO_CONTENT)

        diag_json = DiagnosticoSerializer(diags, many=True).data
        return Response(diag_json, status=status.HTTP_200_OK)

# Intervenciones del evento
class IntervencionesView(EventoView):
    def get(self, request, curp, evento_id, format=None):
        paciente = self.get_pac(curp)
        evento = self.get_evento(evento_id)
        intervenciones = Intervencion.objects.filter(paciente=paciente, evento=evento)

        if not intervenciones:
            return Response({'warning': 'Paciente sin intervenciones'}, status=status.HTTP_204_NO_CONTENT)

        inter_json = IntervencionSerializer(intervenciones, many=True).data
        return Response(inter_json, status=status.HTTP_200_OK)

# Tomas de Signos Vitales del evento
class TomasSignosView(EventoView):
    def get(self, request, curp, evento_id, format=None):
        paciente = self.get_pac(curp)
        evento = self.get_evento(evento_id)
        tomas = Toma.objects.filter(paciente=paciente, evento=evento)

        if not tomas:
            return Response({'warning': 'Paciente sin tomas de signos vitales'}, status=status.HTTP_204_NO_CONTENT)

        tomas_json = TomaSerializer(tomas, many=True).data

        for toma_json in tomas_json:
            signos = SignoVital.objects.filter(toma=toma_json['id'])
            signos_json = SignoVitalSerializer(signos, many=True).data
            toma_json['signos'] = signos_json

        return Response(tomas_json, status=status.HTTP_200_OK)

# Recetas del evento
class RecetasView(EventoView):
    def get(self, request, curp, evento_id, format=None):
        paciente = self.get_pac(curp)
        evento = self.get_evento(evento_id)
        recetas = Receta.objects.filter(paciente=paciente, evento=evento)

        if not recetas:
            return Response({'warning': 'Paciente sin recetas'}, status=status.HTTP_204_NO_CONTENT)

        recetas_json = RecetaSerializer(recetas, many=True).data

        for receta_json in recetas_json:
            meds = Medicamento.objects.filter(receta=receta_json['id'])
            meds_json = MedicamentoSerializer(meds, many=True).data
            receta_json['medicamentos'] = meds_json

        return Response(recetas_json, status=status.HTTP_200_OK)

# Cuestionarios del evento
class CuestionarioView(EventoView):
    def get(self, request, curp, evento_id, format=None):
        paciente = self.get_pac(curp)
        evento = self.get_evento(evento_id)
        cuestionario = Cuestionario.objects.filter(paciente=paciente, evento=evento)

        if not cuestionario:
            return Response({'warning': 'Paciente sin cuestionarios contestados'}, status=status.HTTP_204_NO_CONTENT)

        cuest_json = CuestionarioSerializer(cuestionario, many=True).data
        return Response(cuest_json, status=status.HTTP_200_OK)

# Info de Pacientes
# -----------------------------
# Alergias
class AlergiasView(PacienteView):
    def get(self, request, curp, format=None):
        paciente = self.get_pac(curp)
        alergias = Alergia.objects.filter(paciente=paciente)

        if not alergias:
            return Response({'warning': 'Paciente sin alergias'}, status=status.HTTP_204_NO_CONTENT)

        aler_json = AlergiaSerializer(alergias, many=True).data
        return Response(aler_json, status=status.HTTP_200_OK)

    def post(self, request, curp, format=None):
        self.get_pac(curp)
        serializer = AlergiaSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Medicamentos Tomados en Casa
class MedicamentosView(PacienteView):
    def get(self, request, curp, format=None):
        paciente = self.get_pac(curp)
        medicamentos = Medicamento.objects.filter(paciente=paciente)

        if not medicamentos:
            return Response({'warning': 'Paciente sin medicamentos'}, status=status.HTTP_204_NO_CONTENT)

        meds_json = MedicamentoSerializer(medicamentos, many=True).data
        return Response(meds_json, status=status.HTTP_200_OK)

    def post(self, request, curp, format=None):
        paciente = self.get_pac(curp)
        serializer = MedicamentoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
