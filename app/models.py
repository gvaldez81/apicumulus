from django.db import models
from django.contrib.auth.models import User

class App(models.Model):
    app = models.CharField(max_length=50, default='App')
    credenciales = models.OneToOneField(User, related_name='+')
    admins = models.ManyToManyField(User)

    def __str__(self):
        return "%s" % self.app
