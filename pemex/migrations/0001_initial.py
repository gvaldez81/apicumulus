# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PemexInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numeroEmpleado', models.CharField(max_length=30)),
                ('codigoDerechoHabiente', models.CharField(max_length=5)),
                ('derechoHabiente', models.BooleanField(default=False)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
