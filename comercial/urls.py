
from django.urls import path
from comercial.views import login_usuario, logout_usuario, registro_usuario, actualizar_datos, cerrar_cuenta_usuario, cambiar_contrasenia, agregar_producto_carrito, restar_producto_carrito

urlpatterns = [
    path('login/',login_usuario,name="login"),
    path('logout/',logout_usuario,name="logout"),
    path('registro/',registro_usuario,name="registro"),
    path('datos/<id>',actualizar_datos,name="actualizar_datos"),
    path('cerrar_cuenta/<id>',cerrar_cuenta_usuario,name="cerrar_cuenta"),
    path('cambiar_contrasenia/',cambiar_contrasenia,name="cambiar_contraseña"),
    path("agregar/<int:producto_id>/", agregar_producto_carrito, name="agregar_al_carrito"),
    path("restar/<int:producto_id>/", restar_producto_carrito, name="restar_del_carrito"),
]