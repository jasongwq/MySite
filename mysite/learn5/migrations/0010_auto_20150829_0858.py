# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learn5', '0009_material_member_running_running_material_running_member'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaterialList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('number', models.IntegerField(default=0)),
                ('units', models.CharField(default=b'\xe5\x8d\x95\xe4\xbd\x8d', max_length=4, blank=True)),
                ('total', models.FloatField(default=0)),
                ('remark', models.TextField(blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='material',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='member',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
