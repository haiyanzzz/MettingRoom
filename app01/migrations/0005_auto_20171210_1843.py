# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-10 10:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0004_auto_20171210_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='time',
            name='timeline',
            field=models.TimeField(),
        ),
    ]
