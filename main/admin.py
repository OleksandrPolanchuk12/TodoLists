from django.contrib import admin
from color.models import Color
from rule.models import Rule
from task.models import Task

admin.site.register(Rule)
admin.site.register(Task)
admin.site.register(Color)
