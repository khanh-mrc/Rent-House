# Generated by Django 4.1.3 on 2022-12-05 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0010_listing_lessor'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='status',
            field=models.CharField(choices=[('Available', 'Available'), ('Unvailable', 'Unavailable')], default='Available', max_length=20),
        ),
    ]
