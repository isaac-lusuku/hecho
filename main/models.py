from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(blank=False, unique=True)
    USERNAME_FIELD= "email"

    def __str__(self):
        return self.name
    

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

    def __str__(self):
        return self.name