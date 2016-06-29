# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bbs',
            name='category',
            field=models.ForeignKey(default=1, to='app01.Category'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bbs',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='bbs',
            name='updatad_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]
