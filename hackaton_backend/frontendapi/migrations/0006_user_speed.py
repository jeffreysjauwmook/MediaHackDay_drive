# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontendapi', '0005_user_vim'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='speed',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]
