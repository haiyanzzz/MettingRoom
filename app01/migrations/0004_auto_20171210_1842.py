# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-10 10:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_auto_20171210_1834'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='time',
            options={'verbose_name_plural': '时间表'},
        ),
        migrations.AlterField(
            model_name='time',
            name='timeline',
            field=models.DateField(),
        ),
    ]
