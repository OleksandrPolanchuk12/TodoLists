from django.urls import include, path

urlpatterns = [
    path('', include('main.urls.rules')),
    path('', include('main.urls.tasks')),
    path('', include('main.urls.main')),
    path('', include('main.urls.forgotpassword')),
]