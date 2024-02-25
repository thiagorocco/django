from rest_framework import generics
from .models import Task
from django.shortcuts import render
from django.core.serializers import TaskSerializer


class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


def index(request):
    return render(request, 'index.html')
