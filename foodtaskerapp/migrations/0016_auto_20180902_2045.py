# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-09-02 20:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodtaskerapp', '0015_auto_20180823_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]
