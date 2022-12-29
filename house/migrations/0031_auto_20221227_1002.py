from django.contrib.postgres.operations import UnaccentExtension
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0029_alter_listing_managers_alter_listing_city'),
    ]

    operations = [
        UnaccentExtension()
    ]