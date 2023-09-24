from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .model_forms import *
from django.contrib.auth.forms import UserCreationForm

def welcome_page(request):
    pass


def login_page(request):
    if request.method == "POST":
        user_name = request.POST["username"]
        password = request.POST["password"]

        try:
            user = User.objects.get(username= user_name)
            if user:
                authenticate(request, username=user_name, password=password)
                login(request, user)
                return redirect("home")
        except:
            messages.error(request, "user doesnot not exist")

    context = {}
    return render(request, "main/login_page.html", context)


def logout(request):
    logout(request)
    return redirect("welcome")


def signup_page(request):
    creation = UserCreationForm()
    profile = UserProfile()

    if request.method == "POST":
        c_data = UserCreationForm(request.POST)
        p_data = UserProfile(request.POST)

        if c_data.is_valid() and p_data.is_valid():
            user = c_data.save(commit=False)
            profile = p_data.save(commit=False)
            profile.user = user
            user.username = user.username.lower()
            user.save()
            profile.save()
            login(request, user)
            return redirect('home')

    context = {"creation":creation,
              "profile":profile}
    return render(request, "main/signup_page.html", context)
    


@login_required(login_url="login_page")
def home(request):
    tasks = Task.objects.all(user=request.user)
    context = {"tasks": tasks}
    return render(request, "main/home.html", context)


def user_profile(request):
    pass


def task_page(request):
    pass


# if you can also add in some sort of diaries into the app