# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontendapi', '0004_auto_20150321_1815'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='vim',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]
