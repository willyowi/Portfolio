# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-17 07:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0045_auto_20181017_0844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
