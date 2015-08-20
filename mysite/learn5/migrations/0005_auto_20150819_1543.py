# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learn5', '0004_auto_20150819_1540'),
    ]

    operations = [
        migrations.RenameField(
            model_name='running_material',
            old_name='material',
            new_name='materials',
        ),
        migrations.RenameField(
            model_name='running_material',
            old_name='to2running',
            new_name='runnings',
        ),
        migrations.RenameField(
            model_name='running_member',
            old_name='torunning',
            new_name='running',
        ),
    ]
