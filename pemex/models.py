from django.db import models
from django.utils import timezone
# from pacientes.models import Paciente
from datetime import timedelta

# Create your models here.
class PemexInfo(models.Model):
    # paciente = models.OneToOneField(Paciente)
    numeroEmpleado = models.CharField(max_length=30)
    codigoDerechoHabiente = models.CharField(max_length=5)
    derechoHabiente = models.BooleanField(default=False)
    updated_at = models.DateTimeField(default=timezone.now)

    def is_recent(self):
        return self.updated_at + timedelta(minutes=30) > timezone.now()

    def refresh(self, dh):
        self.derechoHabiente = dh
        self.updated_at = timezone.now()
        self.save()
