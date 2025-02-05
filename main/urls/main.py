from django.shortcuts import redirect
from django.urls import path
from main.views import main

urlpatterns = [
    path('', lambda request: redirect('register')),
    path('home/', main.Home.as_view(), name='home'),
    path('register/', main.Register.as_view(), name='register'),
    path('login/', main.Login.as_view(), name='login'),
    path('logout/', main.logout_view, name='logout'),
]
