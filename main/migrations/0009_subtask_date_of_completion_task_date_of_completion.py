# Generated by Django 4.2.5 on 2023-09-27 20:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_profile_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='subtask',
            name='date_of_completion',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 27, 23, 27, 41, 511006)),
        ),
        migrations.AddField(
            model_name='task',
            name='date_of_completion',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 27, 23, 27, 41, 511006)),
        ),
    ]
