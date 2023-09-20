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
def detalhe_produto(request, produto_id):
    produto = Produto.objects.get(pk=produto_id)
    context = {
        'produto': produto
    }
    return render(request, 'burguer/produto.html', context)