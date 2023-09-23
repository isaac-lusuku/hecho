from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth import authentiacate, login, logout
from django.contrib.auth.decorators import login_required

def welcome_page(request):
    pass


def login_page(request):
    
    context = {}
    return render(request, "main/login_page.html", context)


def register_page(request):
    pass


@login_required(login_url="login_page")
def home(request):
    tasks = Task.objects.all(user=request.user)
    context = {"tasks": tasks}
    return render(request, "main/home.html", context)


def user_profile(request):
    pass


def task_page(request):
    pass