# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-30 23:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20160629_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bbs',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='bbs',
            name='updatad_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
