# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learn5', '0005_auto_20150819_1543'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='running',
            name='runningId',
        ),
    ]
