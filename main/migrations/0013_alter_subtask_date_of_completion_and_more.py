# Generated by Django 4.2.5 on 2023-10-02 18:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_subtask_date_of_completion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subtask',
            name='date_of_completion',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 2, 21, 52, 37, 277398)),
        ),
        migrations.AlterField(
            model_name='task',
            name='date_of_completion',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 2, 21, 52, 37, 277398)),
        ),
    ]
