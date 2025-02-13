from django.contrib.auth import authenticate, logout, login as auth_login
from .tasks import send_email_task
from main.forms import CustomUserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.views import View
import random

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


class ForgotPassword(View):
    def get(self, request):
        return render(request, 'main/forgot-password.html')

    def post(self, request):
        email = request.POST.get('email')
        code = random.randint(100000, 999999)

        user = User.objects.filter(email=email).first()

        if user:
            request.session['email'] = email
            request.session['code'] = str(code)

            send_email_task.delay(email, code)        

            messages.success(
                request, 'Код підтвердження надіслано на вашу пошту!')
            return redirect('confirmation-code')

        messages.error(
            request, 'Користувача з таким ім\'ям та електронною поштою не знайдено.')
        return render(request, 'main/forgot-password.html')


class ConfirmationCode(View):
    def get(self, request):
        return render(request, 'main/confirmation-code.html', {'email': request.session.get('email'), 'code': request.session.get('code')})

    def post(self, request):
        confirmation_code = request.POST.get('code')
        session_code = request.session.get('code')

        if confirmation_code == session_code:
            return redirect('change-password')

        messages.error(request, 'Невірний код підтвердження.')
        return render(request, 'main/confirmation-code.html', {'email': request.session.get('email'), 'code': request.session.get('code')})


class ChangePassword(View):
    def get(self, request):
        return render(request, 'main/change-password.html')

    def post(self, request):

        password = request.POST.get('new_password')
        password1 = request.POST.get('confirm_password')

        if password != password1:
            messages.error(request, 'Паролі не співпадають.')
            return render(request, 'main/change-password.html')

        user = User.objects.get(email=request.session.get('email'))
        user.set_password(password)
        user.save()
        request.session.flush()

        messages.success(
            request, 'Пароль успішно змінено! Тепер ви можете увійти.')
        return redirect('login')

