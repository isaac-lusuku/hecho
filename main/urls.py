from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('reviews/', views.reviews, name="welcome_page"),
    path('login_page/', views.login_page, name="login_page"),
    path('register/', views.Register.as_view(), name="register"),
    path('home/', views.home, name="home"),
    path('user_profile/', views.user_profile, name="user_profile"),
    path('task_page/', views.task_page, name="task_page"),
    path('review/<int:pk>', views.review, name="review"),
    path('test/', views.MyAPIView.as_view(), name="test")
]