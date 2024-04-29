from django.urls import path
from .views import realizar_compra, ver_mis_compras
from .views import DetalleCompra

urlpatterns = [
    path("comprar/", realizar_compra, name="comprar"),
    path("compras/", ver_mis_compras, name="compras"),
    path("detalle-compra/<int:compra_id>/", DetalleCompra.as_view(), name="detalle-compra"),
]