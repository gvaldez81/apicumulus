# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Alergia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('tipo', models.CharField(max_length=1, choices=[(b'M', b'Medicamento'), (b'A', b'Ambiente'), (b'C', b'Comida')])),
                ('severidad', models.CharField(max_length=1, choices=[(b'A', b'Alta'), (b'M', b'Media'), (b'B', b'Baja')])),
                ('reaccion', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Cuestionario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=100)),
                ('pregunta', models.CharField(max_length=100)),
                ('respuesta', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Diagnostico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField()),
                ('nombre', models.CharField(max_length=50)),
                ('codigo', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('medico', models.CharField(max_length=50)),
                ('cedula', models.CharField(max_length=50)),
                ('especialidad', models.CharField(max_length=50)),
                ('tipo', models.CharField(max_length=1, choices=[(b'C', b'Cita'), (b'A', b'Ambulatorio'), (b'H', b'Hospitalizacion'), (b'U', b'Urgencia')])),
                ('fecha', models.DateTimeField()),
                ('motivo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Intervencion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField()),
                ('nombre', models.CharField(max_length=50)),
                ('codigo', models.CharField(max_length=10)),
                ('evento', models.ForeignKey(blank=True, to='pacientes.Evento', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('codigo', models.CharField(max_length=20)),
                ('clasificacion', models.CharField(max_length=20)),
                ('via', models.CharField(max_length=50)),
                ('dosis', models.CharField(max_length=50)),
                ('indicacion', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=20)),
                ('telefonoAlt', models.CharField(max_length=20)),
                ('correo', models.CharField(max_length=30)),
                ('fechaNacimiento', models.DateField()),
                ('sexo', models.CharField(max_length=1, choices=[(b'H', b'Hombre'), (b'M', b'Mujer'), (b'NA', b'No Aplica')])),
                ('curp', models.CharField(unique=True, max_length=20)),
                ('calle', models.CharField(max_length=30)),
                ('codigoPostal', models.CharField(max_length=5)),
                ('ciudad', models.CharField(max_length=30)),
                ('estado', models.CharField(max_length=30)),
                ('pais', models.CharField(max_length=30)),
                ('hospitales', models.ManyToManyField(to='pacientes.Hospital', blank=True)),
                ('owner', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField()),
                ('notas', models.CharField(max_length=100)),
                ('evento', models.ForeignKey(to='pacientes.Evento')),
                ('paciente', models.ForeignKey(to='pacientes.Paciente')),
            ],
        ),
        migrations.CreateModel(
            name='SignoVital',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('valor', models.FloatField()),
                ('nombre', models.CharField(max_length=50)),
                ('unidad', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Toma',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField()),
                ('evento', models.ForeignKey(blank=True, to='pacientes.Evento', null=True)),
                ('paciente', models.ForeignKey(to='pacientes.Paciente')),
            ],
        ),
        migrations.AddField(
            model_name='signovital',
            name='toma',
            field=models.ForeignKey(to='pacientes.Toma'),
        ),
        migrations.AddField(
            model_name='medicamento',
            name='paciente',
            field=models.ForeignKey(blank=True, to='pacientes.Paciente', null=True),
        ),
        migrations.AddField(
            model_name='medicamento',
            name='receta',
            field=models.ForeignKey(blank=True, to='pacientes.Receta', null=True),
        ),
        migrations.AddField(
            model_name='intervencion',
            name='paciente',
            field=models.ForeignKey(to='pacientes.Paciente'),
        ),
        migrations.AddField(
            model_name='evento',
            name='paciente',
            field=models.ForeignKey(to='pacientes.Paciente'),
        ),
        migrations.AddField(
            model_name='diagnostico',
            name='evento',
            field=models.ForeignKey(blank=True, to='pacientes.Evento', null=True),
        ),
        migrations.AddField(
            model_name='diagnostico',
            name='paciente',
            field=models.ForeignKey(to='pacientes.Paciente'),
        ),
        migrations.AddField(
            model_name='cuestionario',
            name='evento',
            field=models.ForeignKey(blank=True, to='pacientes.Evento', null=True),
        ),
        migrations.AddField(
            model_name='cuestionario',
            name='paciente',
            field=models.ForeignKey(to='pacientes.Paciente'),
        ),
        migrations.AddField(
            model_name='alergia',
            name='paciente',
            field=models.ForeignKey(to='pacientes.Paciente'),
        ),
    ]
