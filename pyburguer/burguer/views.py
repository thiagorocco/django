from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    #return HttpResponse('Hello, World!!!')
    return render(request, 'burguer/home.html')
def produto(request):
    return render(request,'burguer/produto.html')