from django.urls import path
from .views import realizar_compra

urlpatterns = [
    path("comprar/", realizar_compra, name="comprar"),
]