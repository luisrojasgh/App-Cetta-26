from django.shortcuts import render, redirect
# from .models import 

# Create your views here.
def login(request):
    titulo="Login"
    
    context={
        "titulo": titulo,
    }
    return render(request, "comercial/login.html", context)