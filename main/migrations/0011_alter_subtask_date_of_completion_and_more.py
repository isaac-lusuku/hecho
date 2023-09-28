# Generated by Django 4.2.5 on 2023-09-28 20:37

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0010_task_public_alter_subtask_date_of_completion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subtask',
            name='date_of_completion',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 28, 23, 37, 17, 184056)),
        ),
        migrations.AlterField(
            model_name='task',
            name='date_of_completion',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 28, 23, 37, 17, 184056)),
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(max_length=50)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]