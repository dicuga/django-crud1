# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-16 21:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '0002_auto_20170414_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='fecha_nacimiento',
            field=models.DateField(blank=True, null=True),
        ),
    ]
