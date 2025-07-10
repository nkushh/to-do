from django.db import models

# Create your models here.
class BaseColumnModel(models.Model):
	date_created = models.DateTimeField(auto_now_add=True)
	created_by = models.ForeignKey('auth_app.UserProfile', null=True, on_delete=models.SET_NULL)
	active_status = models.BooleanField(default=True)

	class Meta:
		abstract = True

class TaskCategory(BaseColumnModel):
	category_name = models.CharField(max_length=255)
	system_defined = models.BooleanField(default=False)

	def __str__(self):
		return self.category_name

class Task(BaseColumnModel):
	task_title = models.CharField(max_length=255)
	category = models.ForeignKey(TaskCategory, null=True, on_delete=models.SET_NULL)
	task_complete = models.BooleanField(default=False)

	def __str__(self):
		return self.task_title
