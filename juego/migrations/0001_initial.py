# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2018-01-03 23:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Resultados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inicio', models.TimeField(default=b'18:14:25')),
                ('tiempo', models.TimeField(blank=True, null=True)),
                ('vidas', models.IntegerField(blank=True, null=True)),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
