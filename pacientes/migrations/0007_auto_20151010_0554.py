# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0006_auto_20151010_0545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='fecha',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='fechaNacimiento',
            field=models.DateField(),
        ),
    ]
