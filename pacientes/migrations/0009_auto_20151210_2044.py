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
                ('app', models.CharField(default=b'App', max_length=50)),
                ('admins', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('credenciales', models.OneToOneField(related_name='+', to=settings.AUTH_USER_MODEL)),
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
        migrations.RemoveField(
            model_name='historia',
            name='paciente',
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='apellido2',
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='segundoNombre',
        ),
        migrations.AddField(
            model_name='medicamento',
            name='clasificacion',
            field=models.CharField(default='None', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paciente',
            name='calle',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paciente',
            name='ciudad',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paciente',
            name='codigoPostal',
            field=models.CharField(default='', max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paciente',
            name='correo',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paciente',
            name='estado',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paciente',
            name='pais',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paciente',
            name='telefono',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paciente',
            name='telefonoAlt',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='alergia',
            name='severidad',
            field=models.CharField(max_length=1, choices=[(b'A', b'Alta'), (b'M', b'Media'), (b'B', b'Baja')]),
        ),
        migrations.AlterField(
            model_name='alergia',
            name='tipo',
            field=models.CharField(max_length=1, choices=[(b'M', b'Medicamento'), (b'A', b'Ambiente'), (b'C', b'Alimentos')]),
        ),
        migrations.AlterField(
            model_name='diagnostico',
            name='codigo',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='diagnostico',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='evento',
            name='tipo',
            field=models.CharField(max_length=1, choices=[(b'C', b'Cita'), (b'A', b'Ambulatorio'), (b'H', b'Hospitalizacion'), (b'U', b'Urgencia')]),
        ),
        migrations.AlterField(
            model_name='intervencion',
            name='codigo',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='intervencion',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='medicamento',
            name='codigo',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='curp',
            field=models.CharField(unique=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='sexo',
            field=models.CharField(max_length=1, choices=[(b'H', b'Hombre'), (b'M', b'Mujer'), (b'NA', b'No Aplica')]),
        ),
        migrations.AlterField(
            model_name='receta',
            name='notas',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='signovital',
            name='valor',
            field=models.FloatField(),
        ),
        migrations.DeleteModel(
            name='Historia',
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
    ]
