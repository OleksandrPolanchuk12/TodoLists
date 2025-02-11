from .models import Rule, Task
from django.forms import ModelForm, TextInput, Select, Textarea, ModelChoiceField

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
