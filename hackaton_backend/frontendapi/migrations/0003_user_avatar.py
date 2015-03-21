# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontendapi', '0002_user_previous_known_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default=b'https://s3-eu-west-1.amazonaws.com/uploads-eu.hipchat.com/68641/1041855/h96g0gxQ2zIY9dz/user_girl2.jpg', upload_to=b'user_avatars/', verbose_name=b'Profilephoto', blank=True),
            preserve_default=True,
        ),
    ]
