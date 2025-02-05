from django.urls import path
from main.views import  rules

urlpatterns = [
    path('home/add_rule', rules.AddRule.as_view(), name='add_rule'),
]
