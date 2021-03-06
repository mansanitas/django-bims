# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-01-09 06:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sass', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteVisit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_visit_date', models.DateField(default=django.utils.timezone.now)),
                ('water_level', models.CharField(blank=True, choices=[(b'DRY', b'Dry'), (b'ISOLATED_POOLS', b'Isolated pools'), (b'MODERATE_FLOW', b'Moderate flow'), (b'HIGH_FLOW', b'High flow'), (b'LOW_FLOW', b'Low flow'), (b'FLOOD', b'Flood')], max_length=100)),
                ('assessor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
