
from django.urls import path
from exhibicion.views import productos_mostrar, productos_mostrar_descuentos

urlpatterns = [
    path('productos/',productos_mostrar,name="productos"),
    path('descuentos/',productos_mostrar_descuentos,name="descuentos")
]