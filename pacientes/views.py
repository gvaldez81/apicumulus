import json
from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse
from .models import Paciente

# Create your views here.
def paciente(request, paciente_id):
    if request.method == 'GET':
        try:
            paciente = Paciente.objects.get(id=paciente_id)
        except Paciente.DoesNotExist:
            pass

        data = serializers.serialize('json', [paciente, ])
        struct = json.loads(data)

        return JsonResponse(struct, safe=False)
