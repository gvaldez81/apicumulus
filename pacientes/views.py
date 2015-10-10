from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .forms import *
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


@csrf_exempt
def paciente(request, paciente_id, hospital_id):
    try:
        paciente = Paciente.objects.get(paciente=paciente_id)
    except Paciente.DoesNotExist:
        return JsonResponse({'error': 'Ese paciente no existe'})

    try:
        hospital = Hospital.objects.get(paciente=paciente_id)
    except Hospital.DoesNotExist:
        return JsonResponse({'error': 'Ese hospital no existe'})

    if request.method == 'POST':
        paciente.hospitales.add(hospital)

        return JsonResponse({'mensaje': 'Se dio permiso al hospital'})

    elif request.method == 'DELETE':
        paciente.hospitales.remove(hospital)

        return JsonResponse({'mensaje': 'Se removio el permiso al hospital'})

    else:
        return JsonResponse({'error': 'No permitido'})


def paciente_por_curp(request, curp):
    if request.method == 'GET':
        try:
            paciente = Paciente.objects.get(curp=curp)
        except Paciente.DoesNotExist:
            return JsonResponse({'error': 'Ese paciente no existe'})

        return JsonResponse({'id': paciente.id})
    else:
        return JsonResponse({'error': 'No permitido'})

# obtiene el paciente solo si el hospital tiene permisos
def paciente_por_hospital(request, curp, hospital_id):
    if request.method == 'GET':
        try:
            paciente = Paciente.objects.get(curp=curp)
        except Paciente.DoesNotExist:
            return JsonResponse({'error': 'Ese paciente no existe'})

        try:
            hospital = paciente.hospitales.get(id=hospital_id)
        except Hospital.DoesNotExist:
            return JsonResponse({'error': 'Ese hospital no tiene permisos'})

        return JsonResponse({'id': paciente.id})
    else:
        return JsonResponse({'error': 'No permitido'})


def eventos(request, paciente_id):
    if request.method == 'GET':
        eventos = Evento.objects.filter(paciente=paciente_id)

        if not eventos:
            return JsonResponse({'warning': 'Paciente sin eventos'})

        eventos_json = to_json(eventos, True)

        for evento_json in eventos_json:
            # tomas
            tomas_json = to_json(Toma.objects.filter(evento=evento_json['id']), True)
            for toma_json in tomas_json:
                signos = SignoVital.objects.filter(toma=toma_json['id'])
                signos_json = to_json(signos, True)
                toma_json['signos'] = signos_json
            evento_json['tomas'] = tomas_json

            # recetas
            recetas_json = to_json(Receta.objects.filter(evento=evento_json['id']), True)
            for receta_json in recetas_json:
                meds = Medicamento.objects.filter(receta=receta_json['id'])
                meds_json = to_json(meds, True)
                receta_json['medicamentos'] = meds_json
            evento_json['recetas'] = recetas_json

            # diagnosticos
            diags_json = to_json(Diagnostico.objects.filter(evento=evento_json['id']), True)
            evento_json['diagnosticos'] = diags_json

            # intervenciones
            inter_json = to_json(Intervencion.objects.filter(evento=evento_json['id']), True)
            evento_json['intervenciones'] = inter_json

        return JsonResponse(eventos_json, safe=False)
    else:
        return JsonResponse({'error': 'No permitido'})


def historia(request, paciente_id):
    if request.method == 'GET':
        try:
            historia = Historia.objects.get(paciente=paciente_id)
        except Historia.DoesNotExist:
            return JsonResponse({'error': 'Ese paciente no existe'})

        hist_json = to_json(historia)
        return JsonResponse(hist_json, safe=False)
    else:
        return JsonResponse({'error': 'No permitido'})

@csrf_exempt
def alergias(request, paciente_id):
    try:
        paciente = Paciente.objects.get(id=paciente_id)
    except Paciente.DoesNotExist:
        return JsonResponse({'error': 'No existe el Usuario'})

    if request.method == 'GET':
        alergias = Alergia.objects.filter(paciente=paciente)

        if not alergias:
            return JsonResponse({'warning': 'Paciente sin alergias'})

        aler_json = to_json(alergias, multi=True)
        return JsonResponse(aler_json, safe=False)

    elif request.method == 'POST':
        form = AlergiaForm(request.POST)

        if form.is_valid():
            alergia = form.save()
            return JsonResponse({'mensaje': 'Alergia creada', 'id': alergia.id})

        return JsonResponse({'error': 'Datos invalidos'})

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

@csrf_exempt
def medicamentos(request, paciente_id):
    if request.method == 'GET':
        medicamentos = Medicamento.objects.filter(paciente=paciente_id)

        if not medicamentos:
            return JsonResponse({'warning': 'Paciente sin medicamentos'})

        meds_json = to_json(medicamentos, multi=True)
        return JsonResponse(meds_json, safe=False)

    elif request.method == 'POST':
        form = MedicamentoForm(request.POST)

        if form.is_valid():
            medicamento = form.save()
            return JsonResponse({'mensaje': 'Medicamento creado', 'id': medicamento.id})

        return JsonResponse({'error': 'Datos invalidos'})

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


def recetas(request, paciente_id):
    if request.method == 'GET':
        recetas = Receta.objects.filter(paciente=paciente_id)

        if not recetas:
            return JsonResponse({'warning': 'Paciente sin recetas'})

        recetas_json = to_json(recetas, True)

        for receta_json in recetas_json:
            meds = Medicamento.objects.filter(receta=receta_json['id'])
            meds_json = to_json(meds, True)
            receta_json['medicamentos'] = meds_json

        return JsonResponse(recetas_json, safe=False)
    else:
        return JsonResponse({'error': 'No permitido'})
