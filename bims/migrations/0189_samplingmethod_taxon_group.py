# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-10-08 06:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bims', '0188_auto_20191008_0606'),
    ]

    operations = [
        migrations.AddField(
            model_name='samplingmethod',
            name='taxon_group',
            field=models.ManyToManyField(blank=True, null=True, to='bims.TaxonGroup'),
        ),
    ]
