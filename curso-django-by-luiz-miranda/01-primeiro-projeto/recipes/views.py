from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def myView(request):
    return HttpResponse('Olá, mundo')