from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.welcome_page, name="welcome_page"),
    path('login_page/', views.login_page, name="login_page"),
    path('signup_page/', views.signup_page, name="signup_page"),
    path('home/', views.home, name="home"),
    path('user_profile/', views.user_profile, name="user_profile"),
    path('task_page/', views.task_page, name="task_page")
]