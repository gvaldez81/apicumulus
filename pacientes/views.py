from django.http import JsonResponse
from .models import *
from .utils import to_json

# Create your views here.
def paciente(request, paciente_id):
    if request.method == 'GET':
        try:
            paciente = Paciente.objects.get(id=paciente_id)
        except Paciente.DoesNotExist:
            return JsonResponse({'error': 'Ese paciente no existe'})

        pac_json = to_json(paciente)
        hosp_json = to_json(paciente.hospitales.all(), True)

        pac_json['hospitales'] = hosp_json

        return JsonResponse(pac_json, safe=False)
    else:
        return JsonResponse({'error': 'No permitido'})

def eventos(request, paciente_id):
    if request.method == 'GET':
        try:
            eventos = Evento.objects.filter(paciente=paciente_id)
        except Evento.DoesNotExist:
            return JsonResponse({'error': 'Paciente sin eventos'})

        eve_json = to_json(eventos, True)

        return JsonResponse(eve_json, safe=False)
    else:
        return JsonResponse({'error': 'No permitido'})
