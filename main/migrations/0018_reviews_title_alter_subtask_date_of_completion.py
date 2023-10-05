# Generated by Django 4.2.5 on 2023-10-05 13:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_alter_reviews_user_alter_subtask_date_of_completion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='title',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='subtask',
            name='date_of_completion',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 5, 16, 7, 49, 133102)),
        ),
    ]
