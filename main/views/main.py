from django.shortcuts import render, redirect
from main.forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login as auth_login
from django.views import View


class Register(View):

    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'main/register.html', {'formregister': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.email = request.POST.get('email')
            user.save()
            messages.success(request, 'Реєстрація успішна!')
            auth_login(request, user)
            return redirect('home')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(
                        request, f"{form.fields[field].label}: {error}")

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