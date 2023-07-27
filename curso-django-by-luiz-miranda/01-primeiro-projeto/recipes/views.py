from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return HttpResponse('<h1>HOME</h1>')

def contato(request):
    return HttpResponse('<h1>CONTATO</h1>')

def sobre(request):
    return HttpResponse('<h1>SOBRE</h1>')