#from exhibicion.models import Producto

def carrito(request):
    carrito = request.session.get('carrito', {})
    return {'carrito': carrito}

