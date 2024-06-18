from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request, 'usuarios/home.html')

def usuarios(request):
    # SALVAR DADOS DO FRONT END PARA O BANCO DE DADOS
    novo_usuario = Usuario()
    novo_usuario.receita = request.POST.get('receita')
    novo_usuario.gasto = request.POST.get('gasto')

    novo_usuario.save()

    # exibir todo a receita e gasto inserido em uma nova pagina
    usuarios ={
        'usuarios': Usuario.objects.all()
    }

    # retornar dados para a pagina de listagem da receita e gasto
    return render(request,'usuarios/usuarios.html', usuarios)
