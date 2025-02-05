from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from django.contrib.auth.models import User
import random


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

        messages.success(
            request, 'Пароль успішно змінено! Тепер ви можете увійти.')
        return redirect('login')
