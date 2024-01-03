from django.shortcuts import render

from exhibicion.models import Producto

# Función 
def productos_mostrar(request):
    titulo="Productos"
    #productos= Producto.objects.all(estado=True)
    context={
        "titulo": titulo,
        #"productos":productos 
    }
    return render(request, "index.html", context)