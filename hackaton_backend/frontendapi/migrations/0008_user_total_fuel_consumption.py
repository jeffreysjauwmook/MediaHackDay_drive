# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontendapi', '0007_user_km_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='total_fuel_consumption',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
