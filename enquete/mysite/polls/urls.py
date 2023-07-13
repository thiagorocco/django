from django.urls import path

from . import views #importe tudo do arquivo views

#Abaixo 
urlpatterns = [
    path('',views.index,name='index')
]