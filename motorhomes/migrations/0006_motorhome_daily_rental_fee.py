# Generated by Django 3.1.5 on 2021-02-02 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motorhomes', '0005_auto_20210201_1750'),
    ]

    operations = [
        migrations.AddField(
            model_name='motorhome',
            name='daily_rental_fee',
            field=models.FloatField(default=100.0),
            preserve_default=False,
        ),
    ]
