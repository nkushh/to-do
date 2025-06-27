from django.contrib import admin
from . import models as auth_models
# Register your models here.
admin.site.register(auth_models.UserProfile)
