from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import RuleForm, TaskForm
from .models import Task
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login as auth_login
from django.views.generic import DeleteView, UpdateView
from django.views import View


class Register(View):

    def get(self, request):
        form = UserCreationForm()
        return render(request, 'main/register.html', {'formregister': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Реєстрація успішна!')
            auth_login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Будь ласка, виправте помилки в формі.')
            return render(request, 'main/register.html', {'formregister': form})


class Login(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return render(request, 'main/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Невірне ім\'я користувача або пароль.')
            return render(request, 'main/login.html')


def logout_view(request):
    logout(request)
    return redirect('register')


class Home(View):

    def get(self, request):
        data = {'user': request.user}
        return render(request, 'main/home.html', data)


class AddRule(View):

    def get(self, request):
        form = RuleForm(initial={'user': request.user})
        return render(request, 'main/add_rule.html', {'form': form, 'error': ''})

    def post(self, request):
        form = RuleForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return render(request, 'main/add_rule.html', {'form': form, 'error': ''})
        else:
            error = 'Форма не правильно заповнена'
            return render(request, 'main/add_rule.html', {'form': form, 'error': error})


class AddTask(View):

    def get(self, request):
        form = TaskForm(initial={'user': request.user})
        return render(request, 'main/add_task.html', {'form': form, 'error': ''})

    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.instance.rule = form.cleaned_data.get('rule', None)
            form.save()
            return render(request, 'main/add_task.html', {'form': form, 'error': ''})
        else:
            error = 'Форма не правильно заповнена'
            return render(request, 'main/add_task.html', {'form': form, 'error': error})


class ViewTasks(View):

    def get(self, request):
        tasks = Task.objects.filter(user=request.user)
        return render(request, 'main/view_tasks.html', {'tasks': tasks})


class TaskEditViews(UpdateView):

    model = Task
    form_class = TaskForm
    template_name = 'main/taskeditviews.html'


class TaskDeleteView(DeleteView):

    model = Task
    template_name = 'main/deletetask.html'
    success_url = '/home/view_tasks'
