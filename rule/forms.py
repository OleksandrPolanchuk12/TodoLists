from .models import Rule
from django.forms import ModelForm, TextInput, Select


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

