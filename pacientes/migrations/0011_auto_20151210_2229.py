# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0010_app_app'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='app',
            name='admins',
        ),
        migrations.RemoveField(
            model_name='app',
            name='credenciales',
        ),
        migrations.DeleteModel(
            name='App',
        ),
    ]
