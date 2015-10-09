# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('segundoNombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('apellido2', models.CharField(max_length=50)),
                ('fechaNacimiento', models.DateField()),
                ('curp', models.CharField(max_length=50)),
                ('sexo', models.CharField(max_length=50, choices=[(b'H', b'Hombre'), (b'M', b'Mujer'), (b'NA', b'No Aplica')])),
            ],
        ),
    ]
