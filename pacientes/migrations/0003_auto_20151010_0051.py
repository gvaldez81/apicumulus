# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0002_auto_20151009_2329'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alergia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(max_length=50, choices=[(b'M', b'Medicamento'), (b'A', b'Ambiente'), (b'C', b'Alimentos')])),
                ('severidad', models.CharField(max_length=50, choices=[(b'A', b'Alta'), (b'M', b'Media'), (b'B', b'Baja')])),
                ('nombre', models.CharField(max_length=50)),
                ('reaccion', models.CharField(max_length=500)),
                ('paciente', models.ForeignKey(to='pacientes.Paciente')),
            ],
        ),
        migrations.CreateModel(
            name='Diagnostico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('codigo', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(max_length=50, choices=[(b'C', b'Cita'), (b'A', b'Ambulatorio'), (b'H', b'Hospitalizacion')])),
                ('fecha', models.DateField()),
                ('medico', models.CharField(max_length=50)),
                ('cedula', models.CharField(max_length=50)),
                ('especialidad', models.CharField(max_length=50)),
                ('motivo', models.CharField(max_length=50)),
                ('paciente', models.ForeignKey(to='pacientes.Paciente')),
            ],
        ),
        migrations.CreateModel(
            name='Historia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('clinica', models.CharField(max_length=1000)),
                ('personal', models.CharField(max_length=1000)),
                ('familiar', models.CharField(max_length=1000)),
                ('paciente', models.ForeignKey(to='pacientes.Paciente')),
            ],
        ),
        migrations.CreateModel(
            name='Intervencion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('codigo', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=100)),
                ('evento', models.ForeignKey(to='pacientes.Evento')),
                ('paciente', models.ForeignKey(to='pacientes.Paciente')),
            ],
        ),
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=50)),
                ('dosis', models.CharField(max_length=50)),
                ('via', models.CharField(max_length=50)),
                ('indicacion', models.CharField(max_length=1000)),
                ('paciente', models.ForeignKey(to='pacientes.Paciente')),
            ],
        ),
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('notas', models.CharField(max_length=1000)),
                ('evento', models.ForeignKey(to='pacientes.Evento')),
                ('paciente', models.ForeignKey(to='pacientes.Paciente')),
            ],
        ),
        migrations.CreateModel(
            name='SignoVital',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('valor', models.FloatField(max_length=50)),
                ('nombre', models.CharField(max_length=50)),
                ('unidad', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Toma',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('evento', models.ForeignKey(to='pacientes.Evento')),
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
            name='receta',
            field=models.ForeignKey(to='pacientes.Receta'),
        ),
        migrations.AddField(
            model_name='diagnostico',
            name='evento',
            field=models.ForeignKey(to='pacientes.Evento'),
        ),
        migrations.AddField(
            model_name='diagnostico',
            name='paciente',
            field=models.ForeignKey(to='pacientes.Paciente'),
        ),
    ]
