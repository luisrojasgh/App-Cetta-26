from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
# from .models import 

# Create your views here.
def login_ususrio(request):
    titulo="Ingreso"
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')

    context={
        "titulo": titulo,
    }
    return render(request, "comercial/login.html", context)