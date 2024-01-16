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

# Función para renderizar los productos de Calzado.
def productos_mostrar_calzado(request):
    titulo="Calzado"
    productos_calzado = Producto.objects.filter(categoria='CALZADO', estado=True)
    context={
        "titulo": titulo,
        "productos_calzado":productos_calzado
    }
    return render(request, "calzado.html", context)

# Función para renderizar los productos de Vestidos.
def productos_mostrar_vestidos(request):
    titulo="Vestidos"
    productos_vestidos = Producto.objects.filter(categoria='VESTIDOS', estado=True)
    context={
        "titulo": titulo,
        "productos_vestidos":productos_vestidos
    }
    return render(request, "vestidos.html", context)

# Función para renderizar los productos de Jeans.
def productos_mostrar_jeans(request):
    titulo="Jeans"
    productos_jeans = Producto.objects.filter(categoria='JEANS', estado=True)
    context={
        "titulo": titulo,
        "productos_jeans":productos_jeans
    }
    return render(request, "jeans.html", context)