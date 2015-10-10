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

def alergias(request, paciente_id):
    if request.method == 'GET':
        try:
            alergias = Alergia.objects.filter(paciente=paciente_id)
        except Alergia.DoesNotExist:
            return JsonResponse({'error': 'Paciente sin alergias'})

        pac_json = to_json(alergias)
        return JsonResponse(pac_json, safe=False)
    else:
        return JsonResponse({'error': 'No permitido'})

def diagnosticos(request, paciente_id):
    if request.method == 'GET':
        try:
            diags = Diagnostico.objects.filter(paciente=paciente_id)
        except Diagnostico.DoesNotExist:
            return JsonResponse({'error': 'Paciente sin diagnosticos'})

        pac_json = to_json(alergias)
        return JsonResponse(pac_json, safe=False)
    else:
        return JsonResponse({'error': 'No permitido'})

def intervenciones(request, paciente_id):
    if request.method == 'GET':
        try:
            alergias = Intervencion.objects.filter(paciente=paciente_id)
        except Intervencion.DoesNotExist:
            return JsonResponse({'error': 'Paciente sin intervenciones'})

        pac_json = to_json(alergias)
        return JsonResponse(pac_json, safe=False)
    else:
        return JsonResponse({'error': 'No permitido'})


