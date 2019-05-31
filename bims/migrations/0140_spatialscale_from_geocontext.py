# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-05-20 09:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bims', '0139_remove_locationsite_boundary'),
    ]

    operations = [
        migrations.AddField(
            model_name='spatialscale',
            name='from_geocontext',
            field=models.BooleanField(default=True, help_text=b'Is this data come from geocontext?'),
        ),
    ]
