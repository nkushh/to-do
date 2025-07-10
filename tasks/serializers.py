from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import ValidationError
from . import models as tasks_models
import datetime

class TaskCategorySerializer(ModelSerializer):
	class Meta:
		model = tasks_models.TaskCategory
		fields = '__all__'

	def create(self, validated_data):
		category_name = validated_data.get('category_name').capitalize()
		validated_data['category_name'] = category_name
		validated_data['created_by'] = self.context['request'].user
		return super().create(validated_data)

class TaskModelSerializer(ModelSerializer):
	class Meta:
		model = tasks_models.Task
		fields = '__all__'

	def create(self, validated_data):
		task_title = validated_data.get('task_title').capitalize()
		user = self.context['request'].user
		date_created = datetime.date.today()

		validated_data['task_title'] = task_title
		validated_data['created_by'] = user
		if tasks_models.Task.objects.filter(task_title=task_title, created_by=user, date_created__date=date_created).exists():
			raise ValidationError("Another task with a similar title exists")
		return super().create(validated_data)