# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-08-07 05:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bims', '0029_auto_20180801_0403'),
    ]

    operations = [
        migrations.AddField(
            model_name='biologicalcollectionrecord',
            name='ready_for_validation',
            field=models.BooleanField(default=False),
        ),
    ]