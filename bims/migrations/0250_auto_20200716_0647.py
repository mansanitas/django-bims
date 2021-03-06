# Generated by Django 2.2.12 on 2020-07-16 06:47

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bims', '0249_auto_20200713_0855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taxonomy',
            name='origin',
            field=models.CharField(blank=True, choices=[('alien', 'Non-Native'), ('indigenous', 'Native'), ('unknown', 'Unknown'), ('alien-invasive', 'Non-native: invasive'), ('alien-non-invasive', 'Non-native: non-invasive')], default='', help_text='Origin', max_length=50),
        ),
        migrations.CreateModel(
            name='HarvestSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(default=datetime.datetime.now)),
                ('category', models.CharField(blank=True, choices=[('gbif', 'GBIF')], default='', max_length=50)),
                ('finished', models.BooleanField(default=False)),
                ('log_file', models.FileField(null=True, upload_to='harvest-session-log/')),
                ('status', models.TextField(blank=True, null=True)),
                ('harvester', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='harvest_session_harvester', to=settings.AUTH_USER_MODEL)),
                ('module_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bims.TaxonGroup')),
            ],
        ),
    ]
