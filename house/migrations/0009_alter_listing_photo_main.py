# Generated by Django 4.1.3 on 2022-12-04 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0008_alter_listing_photo_main'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='photo_main',
            field=models.ImageField(upload_to='photos/%Y/%m/%d/'),
        ),
    ]
