# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0005_auto_20151010_0409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagnostico',
            name='fecha',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='intervencion',
            name='fecha',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='fechaNacimiento',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='receta',
            name='fecha',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='toma',
            name='fecha',
            field=models.DateTimeField(),
        ),
    ]
