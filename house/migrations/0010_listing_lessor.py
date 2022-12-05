# Generated by Django 4.1.3 on 2022-12-04 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_profile_email_profile_name_alter_profile_phone_and_more'),
        ('house', '0009_alter_listing_photo_main'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='lessor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.profile'),
        ),
    ]
