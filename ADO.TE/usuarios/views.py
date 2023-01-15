from django.shortcuts import render
from django.http import HttpResponse 
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants

def cadastro(request):
    if request.method == "GET": 
        return render(request, 'cadastro.html')
    else:
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
        
        if len(nome.strip()) == 0 or len(email.strip()) == 0 or len(senha.strip()) == 0 or len(confirmar_senha.strip()) == 0:
            messages.add_message(request, constants.ERROR, "Preencha todos os Campos!")
            return render(request, 'cadastro.html')
        
        if senha != confirmar_senha:
            messages.add_message(request, constants.ERROR, "Senhas não coincidem!")
            return render(request, 'cadastro.html')
        
        try:
            user = User.objects.create_user(
                username=nome,
                email=email,
                password=senha,
            )
            messages.add_message(request, constants.SUCCESS, "Usuario cadastrado com Sucesso!")
            return render(request, 'cadastro.html')
        except:
            messages.add_message(request, constants.ERROR, "Erro interno do Sistema!")
            return render(request, 'cadastro.html')
    