from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),  # List of tasks
    path('add/', views.add_task, name='add_task'),  # Add new task
    path('complete/<int:task_id>/', views.complete_task, name='complete_task'),  # Mark task as complete
]
