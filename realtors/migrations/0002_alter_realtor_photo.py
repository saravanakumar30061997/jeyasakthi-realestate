# Generated by Django 5.1.6 on 2025-03-04 05:33

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='photo',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='photo'),
        ),
    ]
