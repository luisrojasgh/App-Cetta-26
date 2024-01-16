from django.shortcuts import render, redirect
from .models import Direccion, Usuario

# Create your views here.
def usuario_crear(request):
    titulo="Registro"
    
    context={
        "titulo": titulo,
    }
    return render(request, "comercial/registro.html", context)