from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import ValidationError
from . import models as tasks_models

class TaskModelSerializer(ModelSerializer):
	class Meta:
		model = tasks_models.Task
		fields = '__all__'

	def create(self, validated_data):
		task_title = validated_data.get('task_title').capitalize()
		user = validated_data.get('created_by')
		date_created = validated_data.get('date_created').date()

		validated_data['task_title'] = task_title
		if tasks_models.Task.objects.filter(task_title=task_title, created_by=user, date_created__date=date_created).exists():
			raise ValidationError("Another task with a similar title exists")
		return super().create(validated_data)