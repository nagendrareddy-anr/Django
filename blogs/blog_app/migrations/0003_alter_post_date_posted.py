# Generated by Django 4.2 on 2024-03-31 05:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog_app", "0002_alter_post_date_posted"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="date_posted",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 3, 31, 10, 40, 2, 278414)
            ),
        ),
    ]
