from django.db import models

SEXOS = (
    ('H', 'Hombre'),
    ('M', 'Mujer'),
    ('NA', 'No Aplica'),
)

# Create your models here.
class Paciente(models.Model):
    nombre = models.CharField(max_length=50)
    segundoNombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    apellido2 = models.CharField(max_length=50)
    fechaNacimiento = models.DateField()
    curp = models.CharField(max_length=50)
    sexo = models.CharField(choices=SEXOS, max_length=50)
