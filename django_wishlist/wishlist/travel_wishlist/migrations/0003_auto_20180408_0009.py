# Generated by Django 2.0.4 on 2018-04-08 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel_wishlist', '0002_auto_20180407_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='visited_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]