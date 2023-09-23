from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import *
admin.site.register(UserAdmin)
admin.site.register(Topic)
admin.site.register(Task)
admin.site.register(Subtask)
