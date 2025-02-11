from django.db import models
from django.contrib.auth.models import User
from rule.models import Rule


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
