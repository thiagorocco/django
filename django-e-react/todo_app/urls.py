# todo_app/urls.py
from django.urls import path
from .views import index
from .views import TaskList, TaskDetail

urlpatterns = [
    path('', index, name='index'),
    path('tasks/', TaskList.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
]
