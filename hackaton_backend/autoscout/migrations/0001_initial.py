# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='trip_entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vim', models.CharField(max_length=200)),
                ('timestamp', models.DateTimeField()),
                ('km_total', models.IntegerField(default=0)),
                ('km_diff', models.IntegerField(default=0)),
                ('fuel_total', models.DecimalField(max_digits=99999, decimal_places=2)),
                ('fuel_diff', models.DecimalField(max_digits=99999, decimal_places=2)),
                ('heavy', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
