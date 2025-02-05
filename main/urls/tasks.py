from django.urls import path
from main.views import tasks

urlpatterns = [
    path('home/view_tasks/', tasks.ViewTasks.as_view(), name='view_tasks'),
    path('<int:pk>/update', tasks.TaskEditViews.as_view(), name='edittask'),
    path('<int:pk>/delete', tasks.TaskDeleteView.as_view(), name='deletetask'),
    path('home/add_tasks', tasks.AddTask.as_view(), name='add_task'),
]
