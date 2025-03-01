from django.shortcuts import render
from .forms import TaskForm
from django.views.generic import UpdateView, DeleteView
from .models import Task
from django.views import View


class AddTask(View):

    def get(self, request):
        form = TaskForm(initial={'user': request.user})
        return render(request, 'task/add_task.html', {'form': form, 'error': ''})

    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.instance.rule = form.cleaned_data.get('rule', None)
            form.save()
            return render(request, 'task/add_task.html', {'form': form, 'error': ''})
        else:
            error = 'Форма не правильно заповнена'
            return render(request, 'task/add_task.html', {'form': form, 'error': error})

class ViewTasks(View):

    def get(self, request):
        tasks = Task.objects.filter(user=request.user)
        return render(request, 'task/view_tasks.html', {'tasks': tasks})


class TaskEditViews(UpdateView):

    model = Task
    form_class = TaskForm
    template_name = 'task/task-edit-views.html'


class TaskDeleteView(DeleteView):

    model = Task
    template_name = 'task/delete-task.html'
    success_url = '/home/view_tasks'