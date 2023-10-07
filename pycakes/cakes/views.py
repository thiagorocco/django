from django.shortcuts import render
from cakes.models import Produto

# Create your views here.
def home(request):
    produtos = Produto.objects.all()
    context = {
        'produtos': produtos
    }
    return render(request, 'cakes/home.html', context)
def detalhe_produto(request):
    return render(request, 'cakes/produto.html')