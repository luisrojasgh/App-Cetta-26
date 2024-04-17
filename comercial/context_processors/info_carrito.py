def subtotal_carrito(request):
    subtotal=0
    if request.user.is_authenticated:
        carrito = request.session.get('carrito', {})
        for producto in carrito.values():
            if producto["cantidad"] == 1 and producto["precio_con_descuento"] > 0:
                subtotal=subtotal+int(producto["precio_con_descuento"])
            else:
                subtotal=subtotal+int(producto["precio"])           
    return {"subtotal":subtotal}