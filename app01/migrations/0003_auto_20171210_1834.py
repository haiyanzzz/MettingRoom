# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-10 10:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='time',
            name='timeline',
            field=models.TimeField(),
        ),
    ]
