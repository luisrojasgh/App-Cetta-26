from django.urls import path
from .views import realizar_compra, ver_mis_compras

urlpatterns = [
    path("comprar/", realizar_compra, name="comprar"),
    path("compras/", ver_mis_compras, name="compras"),
]