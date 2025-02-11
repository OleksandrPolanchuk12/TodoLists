from .models import Color
from django.forms import ModelForm

class ColorForm(ModelForm):
    class Meta:
        model = Color
        fields = ['name', 'codcolor']