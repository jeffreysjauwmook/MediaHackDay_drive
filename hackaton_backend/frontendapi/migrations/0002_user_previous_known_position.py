# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import geosimple.fields


class Migration(migrations.Migration):

    dependencies = [
        ('frontendapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='previous_known_position',
            field=geosimple.fields.GeohashField(db_index=True, max_length=12, null=True, blank=True),
            preserve_default=True,
        ),
    ]
