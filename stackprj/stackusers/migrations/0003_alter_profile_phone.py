# Generated by Django 4.0.2 on 2022-02-06 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stackusers', '0002_profile_bio_profile_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
