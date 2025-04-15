from django.forms import EmailField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import forms
from django.utils.translation import gettext_lazy as _


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    def clean_password1(self):
        return self.cleaned_data.get('password1')
    
    def clean_password2(self):
        return self.cleaned_data.get('password2')
        