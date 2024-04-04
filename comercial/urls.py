
from django.urls import path
from comercial.views import login_usuario, logout_usuario, registro_usuario, actualizar_datos, cerrar_cuenta_usuario

urlpatterns = [
    path('login/',login_usuario,name="login"),
    path('logout/',logout_usuario,name="logout"),
    path('registro/',registro_usuario,name="registro"),
    path('datos/<id>',actualizar_datos,name="actualizar_datos"),
    path('cerrar_cuenta/<id>',cerrar_cuenta_usuario,name="cerrar_cuenta")
]