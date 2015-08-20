# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learn5', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Running_Material',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('remark', models.TextField(blank=True)),
                ('material', models.ManyToManyField(to='learn5.Material')),
                ('running', models.ManyToManyField(to='learn5.Running')),
            ],
        ),
        migrations.CreateModel(
            name='Running_Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('remark', models.TextField(blank=True)),
                ('member', models.ManyToManyField(to='learn5.Member')),
                ('running', models.ManyToManyField(to='learn5.Running')),
            ],
        ),
    ]
