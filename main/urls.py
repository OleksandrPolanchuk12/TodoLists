from django.shortcuts import redirect
from django.urls import path
from . import views

urlpatterns = [
    path('', lambda request: redirect('register')),
    path('home/', views.Home.as_view(), name='home'),
    path('register/', views.Register.as_view(), name='register'),
    path('login/', views.Login.as_view(), name='login'),
    path('home/add_rule/', views.AddRule.as_view(), name='add_rule'),
    path('home/add_task/', views.AddTask.as_view(), name='add_task'),
    path('home/view_tasks/', views.ViewTasks.as_view(), name='view_tasks'),
    path('logout/', views.logout_view, name='logout'),
    path('<int:pk>/update', views.TaskEditViews.as_view(), name='edittask'),
    path('<int:pk>/delete', views.TaskDeleteView.as_view(), name='deletetask'),
    path('login/confirmationemail/', views.ForgotPassword.as_view(), name='confirmationemail'),
    path('login/confirmationemail/confirmationcode/', views.ConfirmationCode.as_view(), name='confirmationcode'),
    path('login/confirmationemail/confirmationcode/changepassword/', views.ChangePassword.as_view(), name='changepassword'),
]
