from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from comercial.models import Compra, ItemCompra
from comercial.carrito import Carrito
from django.contrib import messages
from comercial.context_processors.total_carrito import total_carrito

def realizar_compra(request):
    carrito = Carrito(request)
    dato_del_total = total_carrito(request)
    total = dato_del_total['total']
    compra = Compra.objects.create(usuario=request.user, total=total)
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

    carrito.vaciar_carrito()
    messages.success(request, f'Tu compra por $ {total}, ha sido realizada exitosamente.')

    return redirect('productos')

@login_required
def ver_mis_compras(request):
    titulo ='Tus Compras'
    id = request.user.id
    compras_usuario = Compra.objects.filter(usuario_id=id)

    context={
        'titulo':titulo,
        'compras_usuario':compras_usuario
    }
    
    return render(request,'comercial/mis_compras.html',context)





    
