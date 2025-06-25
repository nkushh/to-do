from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Models
from . import models as tasks_models
# Serializers
from . import serializers as tasks_serializers

# Create your views here.
def index(request):
	return render(request, "index.html")

class ListCreateTaskView(generics.ListCreateAPIView):
	queryset = tasks_models.Task.objects.order_by('date_created')
	serializer_class = tasks_serializers.TaskModelSerializer


class FetchUpdateDeleteTaskView(generics.RetrieveUpdateDestroyAPIView):
	queryset = tasks_models.Task.objects.order_by('date_created')
	serializer_class = tasks_serializers.TaskModelSerializer
	lookup_field = 'pk'

