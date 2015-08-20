# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learn5', '0003_auto_20150819_1538'),
    ]

    operations = [
        migrations.RenameField(
            model_name='running_material',
            old_name='running',
            new_name='to2running',
        ),
    ]
