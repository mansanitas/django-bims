# Generated by Django 2.2.12 on 2020-09-24 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bims_theme', '0007_auto_20200910_0702'),
    ]

    operations = [
        migrations.AddField(
            model_name='customtheme',
            name='address_1',
            field=models.TextField(blank=True, default='', help_text='To be displayed in the footer'),
        ),
        migrations.AddField(
            model_name='customtheme',
            name='address_2',
            field=models.TextField(blank=True, default='', help_text='To be displayed in the footer'),
        ),
        migrations.AddField(
            model_name='customtheme',
            name='email_1',
            field=models.CharField(blank=True, default='', help_text='To be displayed in the footer', max_length=200),
        ),
        migrations.AddField(
            model_name='customtheme',
            name='email_2',
            field=models.CharField(blank=True, default='', help_text='To be displayed in the footer', max_length=200),
        ),
        migrations.AddField(
            model_name='customtheme',
            name='facebook_link',
            field=models.URLField(blank=True, default='', help_text='To be displayed in the footer'),
        ),
        migrations.AddField(
            model_name='customtheme',
            name='instagram_link',
            field=models.URLField(blank=True, default='', help_text='To be displayed in the footer'),
        ),
        migrations.AddField(
            model_name='customtheme',
            name='is_footer_enabled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customtheme',
            name='phone_1',
            field=models.CharField(blank=True, default='', help_text='To be displayed in the footer', max_length=200),
        ),
        migrations.AddField(
            model_name='customtheme',
            name='phone_2',
            field=models.CharField(blank=True, default='', help_text='To be displayed in the footer', max_length=200),
        ),
        migrations.AddField(
            model_name='customtheme',
            name='twitter_link',
            field=models.URLField(blank=True, default='', help_text='To be displayed in the footer'),
        ),
    ]
