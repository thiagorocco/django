from django.shortcuts import render
from app.models import Pessoa

def home(request):
    pessoas = Pessoa.objects.all()

    #Isso dará acesso aos dados do banco de dados no template index.html
    return render(request,'app/index.html',{"pessoas": pessoas})

def salvar(request):
    #Cadastrando novo registro
    vnome = request.POST.get("nome")
    #Atributo nome do banco de dados vai receber o valor da variável nome(vnome)
    Pessoa.objects.create(nome=vnome)

    #Atualizando a lista de usuários cadastrados
    pessoas = Pessoa.objects.all()
    return render(request, "app/index.html", {"pessoas":pessoas})