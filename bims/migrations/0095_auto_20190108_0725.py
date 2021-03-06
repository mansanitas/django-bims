# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-01-08 07:25
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bims', '0094_locationsite_other_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='locationsite',
            name='other_data',
        ),
        migrations.AddField(
            model_name='locationsite',
            name='additional_data',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True, verbose_name=b'Additional json data'),
        ),
        migrations.AddField(
            model_name='locationsite',
            name='land_owner_detail',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='locationsite',
            name='map_reference',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
