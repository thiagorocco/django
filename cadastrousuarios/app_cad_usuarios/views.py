from django.shortcuts import render
from .models import Usuario

# Create your views here.
def home(request):
    return render(request,'usuarios/home.html')

def usuarios(request):
    #Salvar os dados da tabela para o banco de dados
    novo_usuario = Usuario()

    #Se passou pelo formulário Post cadastre no BD
    if 'nome' in request.POST and 'idade' in request.POST:
        novo_usuario.nome = request.POST.get('nome')
        novo_usuario.idade = request.POST.get('idade')
        novo_usuario.save()

    #Lista os usuários cadastrados
    usuarios = {
        'usuarios' : Usuario.objects.all()
    }

    return render(request,'usuarios/usuarios.html',usuarios)
