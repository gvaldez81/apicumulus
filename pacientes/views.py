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

        historial = Historia.objects.filter(paciente=paciente)

        if historial:
            hist_json = to_json(historial, True)
        else:
            hist_json = []

        pac_json['hospitales'] = hosp_json
        pac_json['historia'] = hist_json

        return JsonResponse(pac_json, safe=False)
    else:
        return JsonResponse({'error': 'No permitido'})

def eventos(request, paciente_id):
    if request.method == 'GET':
        eventos = Evento.objects.filter(paciente=paciente_id)

        if not eventos:
            return JsonResponse({'warning': 'Paciente sin eventos'})

        eve_json = to_json(eventos, True)

        return JsonResponse(eve_json, safe=False)
    else:
        return JsonResponse({'error': 'No permitido'})

def alergias(request, paciente_id):
    if request.method == 'GET':
        alergias = Alergia.objects.filter(paciente=paciente_id)

        if not alergias:
            return JsonResponse({'warning': 'Paciente sin alergias'})

        aler_json = to_json(alergias, multi=True)
        return JsonResponse(aler_json, safe=False)
    else:
        return JsonResponse({'error': 'No permitido'})

def diagnosticos(request, paciente_id):
    if request.method == 'GET':
        diags = Diagnostico.objects.filter(paciente=paciente_id)

        if not diags:
            return JsonResponse({'warning': 'Paciente sin diagnosticos'})

        diag_json = to_json(diags, multi=True)
        return JsonResponse(diag_json, safe=False)
    else:
        return JsonResponse({'error': 'No permitido'})

def intervenciones(request, paciente_id):
    if request.method == 'GET':
        intervenciones = Intervencion.objects.filter(paciente=paciente_id)

        if not intervenciones:
            return JsonResponse({'warning': 'Paciente sin intervenciones'})

        inter_json = to_json(intervenciones, multi=True)
        return JsonResponse(inter_json, safe=False)
    else:
        return JsonResponse({'error': 'No permitido'})
