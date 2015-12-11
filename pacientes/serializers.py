from .models import *
from rest_framework import serializers

class PacienteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Paciente
        exclude = ()

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        exclude = ()

class CuestionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuestionario
        exclude = ()

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        exclude = ()

class SignoVitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignoVital
        exclude = ()

class TomaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Toma
        exclude = ()

class MedicamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicamento
        exclude = ()

class RecetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receta
        exclude = ()

class DiagnosticoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnostico
        exclude = ()

class IntervencionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intervencion
        exclude = ()

class AlergiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alergia
        exclude = ()
