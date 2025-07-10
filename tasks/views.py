from django.shortcuts import render
from django.db.models import Q
from rest_framework import generics, status
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Models
from . import models as tasks_models
# Serializers
from . import serializers as tasks_serializers
# Libraries
import datetime

# Create your views here.
def index(request):
	return render(request, "index.html")

# TASKS CATEGORIES
def task_categories(request):
	return render(request, "tasks/task_categories.html")

class ListCreateCategoryView(generics.ListCreateAPIView):
	serializer_class = tasks_serializers.TaskCategorySerializer

	permission_classes = [IsAuthenticated]
	authentication_classes = [TokenAuthentication]

	def get_queryset(self):
		return tasks_models.TaskCategory.objects.filter(Q(system_defined=True) | Q(created_by=self.request.user)).order_by('category_name')
	
class FetchUpdateDestroyCategory(generics.RetrieveUpdateDestroyAPIView):
	queryset = tasks_models.TaskCategory.objects.order_by('category_name')
	serializer_class = tasks_serializers.TaskCategorySerializer
	lookup_field = 'pk'

	permission_classes = [IsAuthenticated]
	authentication_classes = [TokenAuthentication]

# TASKS
class ListCreateTaskView(generics.ListCreateAPIView):
	serializer_class = tasks_serializers.TaskModelSerializer

	permission_classes = [IsAuthenticated]
	authentication_classes = [TokenAuthentication]

	def get_queryset(self):
		return tasks_models.Task.objects.filter(created_by=self.request.user).order_by('-pk')


class FetchUpdateDeleteTaskView(generics.RetrieveUpdateDestroyAPIView):
	queryset = tasks_models.Task.objects.order_by('date_created')
	serializer_class = tasks_serializers.TaskModelSerializer
	lookup_field = 'pk'

	permission_classes = [IsAuthenticated]
	authentication_classes = [TokenAuthentication]

class CurrentDayTasksView(generics.ListAPIView):
	date_today = datetime.date.today()
	serializer_class = tasks_serializers.TaskModelSerializer
	print(f'Date: {date_today}')

	permission_classes = [IsAuthenticated]
	authentication_classes = [TokenAuthentication]

	def get_queryset(self):
		return tasks_models.Task.objects.filter(date_created__date=self.date_today, created_by=self.request.user)

class PendingTasksView(generics.ListAPIView):
	serializer_class = tasks_serializers.TaskModelSerializer

	permission_classes = [IsAuthenticated]
	authentication_classes = [TokenAuthentication]

	def get_queryset(self):
		return tasks_models.Task.objects.filter(task_complete=False, created_by=self.request.user)

