# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import  migrations


def create_users(apps, schema_editor):
    User = apps.get_model("frontendapi", "User")
    User.objects.create(
        username='driver1', password='driver1', current_behaviour='none',
        engine_status=1, vim=123
    )
    User.objects.create(
        username='driver2', password='driver2', current_behaviour='none',
        engine_status=1, vim=123
    )


class Migration(migrations.Migration):

    dependencies = [
        ('frontendapi', '0005_user_vim'),
    ]

    operations = [
        migrations.RunPython(create_users),
    ]
