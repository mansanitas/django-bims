# Generated by Django 2.0.4 on 2018-04-17 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bims', '0002_biologicalcollectionrecord'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExampleCollectionRecord',
            fields=[
                ('biologicalcollectionrecord_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='bims.BiologicalCollectionRecord')),
                ('habitat', models.CharField(blank=True, choices=[('euryhaline', 'Euryhaline'), ('freshwater', 'Freshwater')], max_length=50)),
            ],
            bases=('bims.biologicalcollectionrecord',),
        ),
    ]