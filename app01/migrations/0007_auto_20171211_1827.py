# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-11 10:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0006_delete_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='username',
            field=models.CharField(max_length=32, unique=True, verbose_name='用户名'),
        ),
        migrations.AlterUniqueTogether(
            name='reserverecord',
            unique_together=set([('data', 'timeline', 'room')]),
        ),
    ]