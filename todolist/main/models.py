from django.db import models
from django.contrib.auth.models import User
from colorfield.fields import ColorField


class Color(models.Model):
    name = models.CharField(max_length=30)
    codcolor = ColorField()

    def __str__(self):
        return self.name


class Rule(models.Model):
    name = models.CharField(max_length=50)
    color = models.ForeignKey(
        Color, null=True, on_delete=models.CASCADE, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rule = models.ForeignKey(
        Rule, on_delete=models.CASCADE, null=True, blank=True)

    def get_absolute_url(self):
        return '/home/view_tasks'

    def __str__(self):
        return self.name
