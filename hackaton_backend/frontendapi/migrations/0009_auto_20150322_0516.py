# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('frontendapi', '0008_user_total_fuel_consumption'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('started_at', models.DateTimeField()),
                ('ended_at', models.DateTimeField()),
                ('kilometers', models.IntegerField(default=0)),
                ('fuel_consumption', models.FloatField(default=0)),
                ('economy', models.CharField(default=b'economical', max_length=255)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='user',
            name='car_model',
            field=models.CharField(default=b'', max_length=255),
            preserve_default=True,
        ),
    ]
