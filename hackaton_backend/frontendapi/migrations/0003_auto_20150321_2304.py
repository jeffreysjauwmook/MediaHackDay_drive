# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontendapi', '0002_user_previous_known_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='current_behaviour',
            field=models.CharField(default=b'0', max_length=255),
            preserve_default=True,
        ),
    ]
