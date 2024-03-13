from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Usuario
from .forms import RegistroUsuario

# Create your views here.
def login_usuario(request):
    titulo="Ingreso"
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, '¡Bienvenido/a! Has ingresado satisfactoriamente')
            return redirect('index')
        else:
            messages.error(request, 'Error. Usuario o contraseña inválidos')

    context={
        "titulo": titulo,
    }
    return render(request, "comercial/login.html", context)

def logout_usuario(request):
    logout(request)
    messages.success(request, 'Has cerrado sesión satisfactoriamente.')
    return redirect('login')

def registro_usuario(request):
    form = RegistroUsuario()
    titulo="Registro"
    context={
        "titulo": titulo,
        "form": form
    }
    return render(request, "comercial/registro.html", context)
    
    