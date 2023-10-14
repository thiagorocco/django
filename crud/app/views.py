from django.shortcuts import render
from app.models import Pessoa

def home(request):
    pessoas = Pessoa.objects.all()

    #Isso dará acesso aos dados do banco de dados no template index.html
    return render(request,'app/index.html',{"pessoas": pessoas})