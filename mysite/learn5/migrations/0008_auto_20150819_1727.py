# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learn5', '0007_auto_20150819_1717'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='running_material',
            name='materials',
        ),
        migrations.RemoveField(
            model_name='running_material',
            name='runnings',
        ),
        migrations.RemoveField(
            model_name='running_member',
            name='member',
        ),
        migrations.RemoveField(
            model_name='running_member',
            name='running',
        ),
        migrations.DeleteModel(
            name='Material',
        ),
        migrations.DeleteModel(
            name='Member',
        ),
        migrations.DeleteModel(
            name='Running',
        ),
        migrations.DeleteModel(
            name='Running_Material',
        ),
        migrations.DeleteModel(
            name='Running_Member',
        ),
    ]
