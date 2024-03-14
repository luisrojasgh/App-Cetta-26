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
    
    titulo="Registro"
    form = RegistroUsuario(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        username=form.cleaned_data.get('username')
        first_name=form.cleaned_data.get('first_name')
        last_name=form.cleaned_data.get('last_name')
        email=form.cleaned_data.get('email')
        password=form.cleaned_data.get('password')
        #password2=form.cleaned_data.get('password2')
        tipo_documento=form.cleaned_data.get('tipo_documento')
        documento=form.cleaned_data.get('documento')
        numero_telefono=form.cleaned_data.get('numero_telefono')
        numero_celular=form.cleaned_data.get('numero_celular')
        direccion=form.cleaned_data.get('direccion')
        municipio=form.cleaned_data.get('municipio')
        barrio_vereda=form.cleaned_data.get('barrio_vereda')

        print(username,first_name,last_name,email,password,tipo_documento,documento,numero_telefono,numero_celular,direccion,municipio,barrio_vereda)
    
    context={
        "titulo": titulo,
        "form": form
    }
    return render(request, "comercial/registro.html", context)
    