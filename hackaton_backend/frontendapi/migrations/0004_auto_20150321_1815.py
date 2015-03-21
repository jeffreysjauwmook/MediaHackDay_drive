# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontendapi', '0003_auto_20150321_1637'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='owner',
        ),
        migrations.DeleteModel(
            name='Car',
        ),
        migrations.AddField(
            model_name='user',
            name='engine_status',
            field=models.CharField(default='none', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='current_behaviour',
            field=models.CharField(default=b'none', max_length=255),
            preserve_default=True,
        ),
    ]
