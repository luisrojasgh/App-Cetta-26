from django.shortcuts import render, redirect
from configuracion.models import Slider

def principal(request):
    titulo="Bienvenid@s"
    sliders= Slider.objects.filter(estado=True)
    # productos= Producto.objects.all()
    context={
        "titulo": titulo,
        "sliders": sliders,
        # "productos":productos 
    }
    return render(request, "index.html", context)