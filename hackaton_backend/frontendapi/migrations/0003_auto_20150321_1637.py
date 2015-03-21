# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontendapi', '0002_auto_20150321_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='social_score',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
