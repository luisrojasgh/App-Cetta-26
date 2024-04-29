from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from comercial.models import Compra, ItemCompra
from comercial.carrito import Carrito
from django.contrib import messages
from comercial.context_processors.total_carrito import total_carrito
# Importaciones para la generación del pdf
import os
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from django.views import View

@login_required(login_url='/comercial/login')
def realizar_compra(request):
    carrito = Carrito(request)
    dato_del_total = total_carrito(request)
    total = dato_del_total['total']
    compra = Compra.objects.create(usuario=request.user, total=total)
    
    items = list()
    for key, value in carrito.carrito.items():
        items.append(ItemCompra(
            producto_id=key,
            cantidad=value['cantidad'],
            
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

@login_required(login_url='/comercial/login')
def ver_mis_compras(request):
    titulo ='Tus Compras'
    id = request.user.id
    compras_usuario = Compra.objects.filter(usuario_id=id)

    context={
        'titulo':titulo,
        'compras_usuario':compras_usuario
    }
    
    return render(request,'comercial/mis_compras.html',context)

class DetalleCompra(View):
    def get(self, request, *args, **kwargs):
        try:
            template = get_template('comercial/detalle_compra.html')
            compra = get_object_or_404(Compra, pk=self.kwargs['compra_id'])
            detalles = ItemCompra.objects.filter(compra=compra)

            context={
                'detalles': detalles,
                'compra': compra
            }  
            
            html = template.render(context)
            response = HttpResponse(content_type='application/pdf')
            #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
            # Se crea el pdf
            pisa_status = pisa.CreatePDF(
                html, dest=response)
            
            return response
        except:
            pass
        return HttpResponseRedirect(reverse_lazy('compras'))

        

    

        





    
