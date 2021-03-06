# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-03 09:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bims', '0075_taxongroup'),
    ]

    operations = [
        migrations.AddField(
            model_name='taxonidentifier',
            name='iucn_data',
            field=models.TextField(blank=True, null=True, verbose_name=b'Data from IUCN'),
        ),
        migrations.AddField(
            model_name='taxonidentifier',
            name='iucn_redlist_id',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'IUCN taxon id'),
        ),
        migrations.AddField(
            model_name='taxonidentifier',
            name='iucn_status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bims.IUCNStatus', verbose_name=b'IUCN status'),
        ),
    ]
