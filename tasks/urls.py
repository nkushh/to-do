from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
	path('', views.index, name='home'),
	path('tasks/', views.ListCreateTaskView.as_view(), name='tasks'),
	path('task-detail/<int:pk>/', views.FetchUpdateDeleteTaskView.as_view(), name='task_detail'),
]