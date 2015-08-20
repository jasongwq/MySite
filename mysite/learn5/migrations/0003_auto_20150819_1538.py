# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learn5', '0002_running_material_running_member'),
    ]

    operations = [
        migrations.RenameField(
            model_name='running_member',
            old_name='running',
            new_name='torunning',
        ),
    ]
