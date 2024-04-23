from django.shortcuts import render, redirect
from comercial.models import Compra, ItemCompra
from comercial.carrito import Carrito
from django.contrib import messages
from comercial.context_processors.info_carrito import subtotal_carrito

def realizar_compra(request):
    carrito = Carrito(request)
    dato_del_subtotal = subtotal_carrito(request)
    subtotal = dato_del_subtotal['subtotal']
    compra = Compra.objects.create(usuario=request.user, subtotal=subtotal)
    #carro = request.session.carrito
    items = list()
    for key, value in carrito.carrito.items():
        items.append(ItemCompra(
            producto_id=key,
            cantidad=value['cantidad'],
            #usuario=request.user,
            compra=compra
        ))
    
    ItemCompra.objects.bulk_create(items)

    """ enviar_mail(
        compra=compra,
        items=items,
        nombre_usuario=request.user.first_name,
        email=request.user.email,
    ) """

    messages.success(request, 'Tu compra ha sido realizada exitosamente.')

    return redirect('productos')

    
