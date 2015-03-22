# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontendapi', '0006_user_eco_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='km_total',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
