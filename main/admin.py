from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

# Register your models here.

admin.site.register(Profile)
admin.site.register(Topic)
admin.site.register(Task)
admin.site.register(Subtask)
