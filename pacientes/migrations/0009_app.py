# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pacientes', '0008_paciente_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('admins', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('credenciales', models.OneToOneField(related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
