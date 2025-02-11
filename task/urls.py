from django.urls import path
from . import views

urlpatterns = [
    path('home/view_tasks/', views.ViewTasks.as_view(), name='view_tasks'),
    path('<int:pk>/update', views.TaskEditViews.as_view(), name='edittask'),
    path('<int:pk>/delete', views.TaskDeleteView.as_view(), name='deletetask'),
    path('home/add_tasks', views.AddTask.as_view(), name='add_task'),
]
