# Generated by Django 5.0.2 on 2024-03-10 14:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_contact_delete_contacts'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='listing',
            new_name='listing_name',
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 3, 10, 20, 0, 53, 858262)),
        ),
    ]
