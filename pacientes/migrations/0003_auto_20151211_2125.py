# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0002_auto_20151211_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='owner',
            field=models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
