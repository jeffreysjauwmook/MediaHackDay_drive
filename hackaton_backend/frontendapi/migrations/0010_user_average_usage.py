# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontendapi', '0009_auto_20150322_0516'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='average_usage',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
