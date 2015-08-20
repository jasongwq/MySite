# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=4)),
                ('number', models.IntegerField(default=0)),
                ('units', models.CharField(default=b'\xe5\x8d\x95\xe4\xbd\x8d', max_length=4, blank=True)),
                ('total', models.FloatField(default=0)),
                ('remark', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=4)),
                ('funds', models.FloatField(default=0.0)),
                ('remark', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Running',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('runningId', models.CharField(max_length=30)),
                ('itemtime', models.DateField(auto_now_add=True)),
                ('itemname', models.CharField(max_length=30)),
                ('remark', models.TextField(blank=True)),
            ],
        ),
    ]
