from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
	path('', views.index, name='home'),
	path('tasks/', views.ListCreateTaskView.as_view(), name='tasks'),
	path('task-detail/<int:pk>/', views.FetchUpdateDeleteTaskView.as_view(), name='task_detail'),
	path('tasks-today/', views.CurrentDayTasksView.as_view(), name='tasks_today'),
	path('pending-tasks/', views.PendingTasksView.as_view(), name='pending_tasks'),
]