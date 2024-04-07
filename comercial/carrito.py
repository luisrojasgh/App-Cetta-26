from exhibicion.models import Producto

# carrito.py
class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get('carrito')
        if not carrito:
            carrito = self.session['carrito'] = {}

        self.carrito = carrito

    def agregar_producto(self, producto_id, cantidad):
        producto_id = str(producto_id)
        if producto_id not in self.carrito:
            self.carrito[producto_id] = {'cantidad': 0}

        self.carrito[producto_id]['cantidad'] += cantidad
        self.guardar_carrito()

    def quitar_producto(self, producto_id, cantidad):
        producto_id = str(producto_id)
        if producto_id in self.carrito:
            self.carrito[producto_id]['cantidad'] -= cantidad
            if self.carrito[producto_id]['cantidad'] <= 0:
                del self.carrito[producto_id]

        self.guardar_carrito()

    def limpiar_carrito(self):
        self.session['carrito'] = {}
        self.session.modified = True

    def guardar_carrito(self):
        self.session['carrito'] = self.carrito
        self.session.modified = True