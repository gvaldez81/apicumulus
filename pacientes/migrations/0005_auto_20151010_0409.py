# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0004_auto_20151010_0102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagnostico',
            name='evento',
            field=models.ForeignKey(blank=True, to='pacientes.Evento', null=True),
        ),
        migrations.AlterField(
            model_name='intervencion',
            name='evento',
            field=models.ForeignKey(blank=True, to='pacientes.Evento', null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='curp',
            field=models.CharField(unique=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='toma',
            name='evento',
            field=models.ForeignKey(blank=True, to='pacientes.Evento', null=True),
        ),
    ]
