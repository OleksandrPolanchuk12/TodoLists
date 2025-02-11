from django.db import models
from django.contrib.auth.models import User
from color.models import Color


class Rule(models.Model):
    name = models.CharField(max_length=50)
    color = models.ForeignKey(
        Color, null=True, on_delete=models.CASCADE, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
