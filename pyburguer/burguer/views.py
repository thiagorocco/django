from django.shortcuts import render
from burguer.models import Produto
from django.http import HttpResponse



# Create your views here.
def home(request):
    #return HttpResponse('Hello, World!!!')
    produtos = Produto.objects.all()
    context = {
        'produtos' : produtos
    }
    return render(request, 'burguer/home.html',context)
def produto(request):
    return render(request,'burguer/produto.html')