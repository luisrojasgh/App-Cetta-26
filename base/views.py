from django.shortcuts import render, redirect
from configuracion.models import Slider, DescuentoInformacion, DescuentoImagen, ProductoIndex

def principal(request):
    titulo="Bienvenid@s"
    sliders= Slider.objects.filter(estado=True)
    info_descuento= DescuentoInformacion.objects.filter(estado=True)
    imagenes= DescuentoImagen.objects.filter(estado=True)
    producto_index= ProductoIndex.objects.filter(estado=True)
    # productos= Producto.objects.all()
    context={
        "titulo": titulo,
        "sliders": sliders,
        "info_descuento": info_descuento,
        "imagenes": imagenes,
        "producto_index": producto_index,
        # "productos":productos 
    }
    return render(request, "index.html", context)