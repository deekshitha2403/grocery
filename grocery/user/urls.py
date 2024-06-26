from django.urls import path
from .views import register_user,login_user,dashboard

urlpatterns = [
    path("register-user/", register_user),
    path("login-user/",login_user),
    path('dashboard/',dashboard)
]