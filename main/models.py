from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    # contact = models.IntegerField(max_length=15, blank=True, unique=True, null=False)
    email = models.EmailField(max_length=20, blank=False, unique=True)
    # image=models.ImageField(default='default.jpg',upload_to='profile_pics')

# you should make sure you read bout the signals

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()


class Topic(models.Model):
    name = models.CharField(blank=False, max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)

    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    name = models.CharField(blank=False, null=False, max_length=20)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date_created = models.DateTimeField(null=False, blank=False)
    deadline = models.DateTimeField(max_length=50, blank=True)
    completed = models.BooleanField(default=False)
    description = models.TextField(max_length=50, blank=False)
    date_of_completion = models.DateTimeField(default=datetime.datetime.now())
    

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ['-deadline']
    

class Subtask(models.Model):
    name = models.CharField(max_length=20, blank=False)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, blank=False)
    description = models.TextField(blank=False, max_length=40)
    deadline = models.DateTimeField(blank=False)
    completed = models.BooleanField(default=False)
    date_of_completion = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.name
    

# add reviews and profile pictures for the users