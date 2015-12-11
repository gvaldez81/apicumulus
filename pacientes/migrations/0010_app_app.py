# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0009_app'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='app',
            field=models.CharField(default=b'App', max_length=50),
        ),
    ]
