# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-15 14:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0036_auto_20181015_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 15, 14, 6, 31, 734085, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='review',
            name='average',
            field=models.DecimalField(decimal_places=3, default=1, max_digits=10),
        ),
    ]
