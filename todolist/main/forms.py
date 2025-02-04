from .models import Rule, Task, Color
from django.forms import ModelForm, TextInput, Select, Textarea, ModelChoiceField, EmailField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import forms


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    def clean_password1(self):
        return self.cleaned_data.get('password1')
    
    def clean_password2(self):
        return self.cleaned_data.get('password2')
        

class ColorForm(ModelForm):
    class Meta:
        model = Color
        fields = ['name', 'codcolor']


class RuleForm(ModelForm):
    class Meta:
        model = Rule
        fields = ['name', 'color', 'user']

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Назва',

            }),
            'color': Select(attrs={
                'class': 'form-control',

            }),
            'user': Select(attrs={
                'class': 'form-control',
                # 'disabled': 'disabled',

            }),

        }


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'rule', 'user']
        rule = ModelChoiceField(queryset=Rule.objects.all(), required=False)
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Назва',

            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Опис задачі',

            }),
            'rule': Select(attrs={
                'class': 'form-control',

            }),
            'user': Select(attrs={
                'class': 'form-control',

            }),
        }

