# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2018-01-03 23:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juego', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resultados',
            name='inicio',
        ),
        migrations.AddField(
            model_name='resultados',
            name='pistas',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
