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

        eventos_json = to_json(eventos, True)

        for evento_json in eventos_json:
	    
            tomas_json = to_json(Tomas.objects.filter(evento=evento_json['id']), True)

            for toma_json in tomas_json:
                signos = SignoVital.objects.filter(toma=toma_json['id'])
                signos_json = to_json(signos, True)
	        toma_json['signos'] = signos_json

            evento_json['tomas'] = tomas_json

	    recetas_json = to_json(Receta.objects.filter(evento=evento_json['id']), True)

            for receta_json in recetas_json:
                meds = Medicamento.objects.filter(receta=receta_json['id'])
                meds_json = to_json(meds, True)
	        receta_json['medicamentos'] = meds_json

	    evento_json['recetas'] = recetas_json

	    diags_json = to_json(Diagnostico.objects.filter(evento=evento_json['id']), True)
	    evento_json['diagnosticos'] = diags_json

	    inter_json = to_json(Intervencion.objects.filter(evento=evento_json['id']), True)
	    evento_json['intervenciones'] = inter_json

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


def medicamentos(request, paciente_id):
    if request.method == 'GET':
        medicamentos = Medicamento.objects.filter(paciente=paciente_id)

        if not medicamentos:
            return JsonResponse({'warning': 'Paciente sin medicamentos'})

        meds_json = to_json(medicamentos, multi=True)
        return JsonResponse(meds_json, safe=False)
    else:
        return JsonResponse({'error': 'No permitido'})


def tomas_signos(request, paciente_id):
    if request.method == 'GET':
        tomas = Toma.objects.filter(paciente=paciente_id)

        if not tomas:
            return JsonResponse({'warning': 'Paciente sin tomas de signos vitales'})
        
	tomas_json = to_json(tomas, True)

        for toma_json in tomas_json:
            signos = SignoVital.objects.filter(toma=toma_json['id'])
	    signos_json = to_json(signos, True)
	    toma_json['signos'] = signos_json

        return JsonResponse(tomas_json, safe=False)
    else:
        return JsonResponse({'error': 'No permitido'})

