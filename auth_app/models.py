from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from tasks.models import BaseColumnModel

# Create your models here.
class UserProfile(AbstractUser, BaseColumnModel):
	role = models.ForeignKey(Group, null=True, on_delete=models.SET_NULL)
	
	def __str__(self):
		return self.email
