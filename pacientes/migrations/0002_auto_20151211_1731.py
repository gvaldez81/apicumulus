# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='evento',
            old_name='fecha',
            new_name='fechaInicio',
        ),
        migrations.AddField(
            model_name='evento',
            name='fechaFin',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paciente',
            name='apellidoSegundo',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
