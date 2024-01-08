from django.shortcuts import render
from django.db.models import Q
from exhibicion.models import Producto

# Función para renderizar los productos.
def productos_mostrar(request):
    titulo="Productos"
    productos= Producto.objects.filter(estado=True)
    context={
        "titulo": titulo,
        "productos":productos 
    }
    return render(request, "productos.html", context)

# Función para renderizar los productos en descuento.
def productos_mostrar_descuentos(request):
    titulo="Ofertas"
    productos_descuento = Producto.objects.filter(descuento__gt=0, estado=True)
    context={
        "titulo": titulo,
        "productos_descuento":productos_descuento 
    }
    return render(request, "descuentos.html", context)