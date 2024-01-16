
from django.urls import path
from comercial.views import usuario_crear

urlpatterns = [
    path('registro/',usuario_crear,name="registro"),
   
]