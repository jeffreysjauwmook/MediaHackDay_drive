# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontendapi', '0005_auto_20150321_2350'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='eco_score',
            field=models.CharField(default=b'neutral', max_length=255),
            preserve_default=True,
        ),
    ]
