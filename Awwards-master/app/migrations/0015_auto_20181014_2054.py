# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-14 17:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20181013_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 14, 17, 54, 57, 687976, tzinfo=utc)),
        ),
    ]
