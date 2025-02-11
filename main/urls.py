from django.shortcuts import redirect
from django.urls import path
from . import views

urlpatterns = [
    path('', lambda request: redirect('register')),
    path('home/', views.Home.as_view(), name='home'),
    path('register/', views.Register.as_view(), name='register'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('login/confirmationemail/',
         views.ForgotPassword.as_view(), name='confirmation-email'),
    path('login/confirmationemail/confirmationcode/',
         views.ConfirmationCode.as_view(), name='confirmation-code'),
    path('login/confirmationemail/confirmationcode/changepassword/',
         views.ChangePassword.as_view(), name='change-password'),
]
