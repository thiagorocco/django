from django.urls import path
from .views import angular_demo

urlpatterns = [
    path('angular-demo/', angular_demo, name='angular-demo'),
]
