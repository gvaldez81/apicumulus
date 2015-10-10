from django.db import models

SEXOS = (
    ('H', 'Hombre'),
    ('M', 'Mujer'),
    ('NA', 'No Aplica'),
)

ALER_TIPO = (
    ('M', 'Medicamento'),
    ('A', 'Ambiente'),
    ('C', 'Alimentos'),
)

ALER_SEVER = (
    ('A', 'Alta'),
    ('M', 'Media'),
    ('B', 'Baja'),
)

EVENT_TIPO = (
    ('C', 'Cita'),
    ('A', 'Ambulatorio'),
    ('H', 'Hospitalizacion'),
)

# Create your models here.
class Hospital(models.Model):
    nombre = models.CharField(max_length=50)

class Paciente(models.Model):
    nombre = models.CharField(max_length=50)
    segundoNombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    apellido2 = models.CharField(max_length=50)
    fechaNacimiento = models.DateField()
    curp = models.CharField(max_length=50)
    sexo = models.CharField(choices=SEXOS, max_length=50)
    hospitales = models.ManyToManyField(Hospital)

class Evento(models.Model):
    tipo = models.CharField(choices=EVENT_TIPO, max_length=50)
    fecha = models.DateField()
    medico = models.CharField(max_length=50)
    cedula = models.CharField(max_length=50)
    especialidad = models.CharField(max_length=50)
    motivo = models.CharField(max_length=50)
    paciente = models.ForeignKey(Paciente)

class Alergia(models.Model):
    tipo = models.CharField(choices=ALER_TIPO, max_length=50)
    severidad = models.CharField(choices=ALER_SEVER, max_length=50)
    nombre = models.CharField(max_length=50)
    reaccion = models.CharField(max_length=500)
    paciente = models.ForeignKey(Paciente)

class Diagnostico(models.Model):
    fecha = models.DateField()
    evento = models.ForeignKey(Evento)
    codigo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=100)
    paciente = models.ForeignKey(Paciente)

class Intervencion(models.Model):
    fecha = models.DateField()
    evento = models.ForeignKey(Evento)
    codigo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=100)
    paciente = models.ForeignKey(Paciente)

class Historia(models.Model):
    clinica = models.CharField(max_length=1000)
    personal = models.CharField(max_length=1000)
    familiar = models.CharField(max_length=1000)
    paciente = models.ForeignKey(Paciente)

class Receta(models.Model):
    fecha = models.DateField()
    evento = models.ForeignKey(Evento)
    notas = models.CharField(max_length=1000)
    paciente = models.ForeignKey(Paciente)

class Medicamento(models.Model):
    codigo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    dosis = models.CharField(max_length=50)
    via = models.CharField(max_length=50)
    indicacion = models.CharField(max_length=1000)
    paciente = models.ForeignKey(Paciente, null=True, blank=True)
    receta = models.ForeignKey(Receta, null=True, blank=True)

class Toma(models.Model):
    fecha = models.DateField()
    evento = models.ForeignKey(Evento)
    paciente = models.ForeignKey(Paciente)

class SignoVital(models.Model):
    valor = models.FloatField(max_length=50)
    nombre = models.CharField(max_length=50)
    unidad = models.CharField(max_length=50)
    toma = models.ForeignKey(Toma)
