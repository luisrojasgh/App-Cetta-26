def subtotal_carrito(request):
    subtotal=0
    if request.user.is_authenticated:
        carrito = request.session.get('carrito', {})
        for producto in carrito.values():
            subtotal=subtotal+int(producto["precio"])
           
    return {"subtotal":subtotal}