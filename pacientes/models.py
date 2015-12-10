from django.db import models
from django.contrib.auth.models import User

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
    ('U', 'Urgencia'),
)

# Create your models here.
class Hospital(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Paciente(models.Model):
    owner = models.OneToOneField(User)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    telefonoAlt = models.CharField(max_length=20)
    correo = models.CharField(max_length=30)
    fechaNacimiento = models.DateField()
    sexo = models.CharField(choices=SEXOS, max_length=1)
    curp = models.CharField(max_length=20, unique=True)
    calle = models.CharField(max_length=30)
    codigoPostal = models.CharField(max_length=5)
    ciudad = models.CharField(max_length=30)
    estado = models.CharField(max_length=30)
    pais = models.CharField(max_length=30)
    hospitales = models.ManyToManyField(Hospital)

    def __str__(self):
        return "%s %s %s %s" % (self.nombre, self.segundoNombre, self.apellido, self.apellido2)

class Evento(models.Model):
    medico = models.CharField(max_length=50)
    cedula = models.CharField(max_length=50)
    especialidad = models.CharField(max_length=50)
    tipo = models.CharField(choices=EVENT_TIPO, max_length=1)
    fecha = models.DateTimeField()
    motivo = models.CharField(max_length=50)
    paciente = models.ForeignKey(Paciente)

    def __str__(self):
        return "%s - %s" % (self.tipo, self.fecha.strftime('%Y-%m-%d'))

class Alergia(models.Model):
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(choices=ALER_TIPO, max_length=1)
    severidad = models.CharField(choices=ALER_SEVER, max_length=1)
    reaccion = models.CharField(max_length=500)
    paciente = models.ForeignKey(Paciente)

    def __str__(self):
        return "%s %s %s" % (self.nombre, self.tipo, self.severidad)

class Diagnostico(models.Model):
    fecha = models.DateTimeField()
    nombre = models.CharField(max_length=50)
    codigo = models.CharField(max_length=10)
    evento = models.ForeignKey(Evento, null=True, blank=True)
    paciente = models.ForeignKey(Paciente)

    def __str__(self):
        return "%s %s - %s" % (self.nombre, self.codigo, self.fecha.strftime('%Y-%m-%d'))

class Intervencion(models.Model):
    fecha = models.DateTimeField()
    nombre = models.CharField(max_length=50)
    codigo = models.CharField(max_length=10)
    evento = models.ForeignKey(Evento, null=True, blank=True)
    paciente = models.ForeignKey(Paciente)

    def __str__(self):
        return "%d %s" % (self.id, self.nombre)

class Cuestionario(models.Model):
    titulo = models.CharField(max_length=100)
    pregunta = models.CharField(max_length=100)
    respuesta = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    evento = models.ForeignKey(Evento, null=True, blank=True)
    paciente = models.ForeignKey(Paciente)

    def __str__(self):
        return "%d %s" % (self.id, self.paciente.id)

class Receta(models.Model):
    fecha = models.DateTimeField()
    notas = models.CharField(max_length=100)
    evento = models.ForeignKey(Evento)
    paciente = models.ForeignKey(Paciente)

    def __str__(self):
        return "%d %s" % (self.id, self.paciente.id)

class Medicamento(models.Model):
    nombre = models.CharField(max_length=50)
    codigo = models.CharField(max_length=20)
    clasificacion = models.CharField(max_length=20)
    via = models.CharField(max_length=50)
    dosis = models.CharField(max_length=50)
    indicacion = models.CharField(max_length=1000)
    receta = models.ForeignKey(Receta, null=True, blank=True)
    paciente = models.ForeignKey(Paciente, null=True, blank=True)

    def __str__(self):
        return "%d %s" % (self.id, self.codigo)

class Toma(models.Model):
    fecha = models.DateTimeField()
    evento = models.ForeignKey(Evento, null=True, blank=True)
    paciente = models.ForeignKey(Paciente)

    def __str__(self):
        return "%d %s" % (self.id, self.paciente.id)

class SignoVital(models.Model):
    valor = models.FloatField()
    nombre = models.CharField(max_length=50)
    unidad = models.CharField(max_length=50)
    toma = models.ForeignKey(Toma)

    def __str__(self):
        return "%d %s" % (self.id, self.valor)

class App(models.Model):
    app = models.CharField(max_length=50, default='App')
    credenciales = models.OneToOneField(User, related_name='+')
    admins = models.ManyToManyField(User)

    def __str__(self):
        return "%s" % self.app
