from django.db import models
from colorfield.fields import ColorField


class Color(models.Model):
    name = models.CharField(max_length=30)
    codcolor = ColorField()

    def __str__(self):
        return self.name
