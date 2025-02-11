from django.urls import path
from . import  views

urlpatterns = [
    path('home/add_rule', views.AddRule.as_view(), name='add_rule'),
]
