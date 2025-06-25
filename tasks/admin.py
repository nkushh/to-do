from django.contrib import admin
from . import models as tasks_models

# Register your models here.
admin.site.register(tasks_models.Task)