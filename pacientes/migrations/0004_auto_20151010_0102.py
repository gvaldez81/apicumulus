# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0003_auto_20151010_0051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicamento',
            name='paciente',
            field=models.ForeignKey(blank=True, to='pacientes.Paciente', null=True),
        ),
        migrations.AlterField(
            model_name='medicamento',
            name='receta',
            field=models.ForeignKey(blank=True, to='pacientes.Receta', null=True),
        ),
    ]
