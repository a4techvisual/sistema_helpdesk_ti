from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == "POST":
        username = request.POST.get('username','').strip()
        password = request.POST.get('password','')
        user = authenticate(request,username=username,password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('index')

        return render(request, 'login.html', {
            'error': "Nome do usuário ou senha inválidos."
        })
    return render(request, "login.html")

def novo_usuario(request):
    if request.method == "POST":
        username = request.POST.get('username','').strip()
        password = request.POST.get('password','')
        confirm_password = request.POST.get('confirm_password','')

        if not username:
            return render(request, 'novo-usuario.html',{
                'error': "Informe o nome do usuário."
            })

        if password != confirm_password:
            return render(request, 'novo-usuario.html',{
                'error': "As senhas não são iguais."
            })

        if User.objects.filter(username=username).exists():
            return render(request, 'novo-usuario.html',{
                'error': "Este usuário já está cadastrado."
            })

        User.objects.create_user(username=username,password=password)
        messages.success(request, "Conta criada! Faça o login para continuar.")
        return redirect('login')
    return render(request, "novo-usuario.html")

def logout(request):
    auth_logout(request)
    return redirect('login')