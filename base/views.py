from django.shortcuts import render, redirect
from configuracion.models import Slider, DescuentoInformacion, DescuentoImagen, ProductoIndex

# Función para renderizar el contexto en index.html
def principal(request):
    titulo="Bienvenid@s"
    sliders= Slider.objects.filter(estado=True)
    info_descuento= DescuentoInformacion.objects.filter(estado=True)
    imagenes= DescuentoImagen.objects.filter(estado=True)
    producto_index= ProductoIndex.objects.filter(estado=True)
    
    context={
        "titulo": titulo,
        "sliders": sliders,
        "info_descuento": info_descuento,
        "imagenes": imagenes,
        "producto_index": producto_index,
    }
    return render(request, "index.html", context)

def ayuda_usuario(request):
    titulo="Ayuda"
    context={
        "titulo": titulo,
    }
    return render(request, "ayuda.html", context)

def preguntas(request):
    titulo="Preguntas frecuentes"
    context={
        "titulo": titulo,
    }
    return render(request, "preguntas.html", context)

def contacto(request):
    titulo="Atención y contacto"
    context={
        "titulo": titulo,
    }
    return render(request, "contacto.html", context)