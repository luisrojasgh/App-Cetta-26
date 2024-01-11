
from django.urls import path
from exhibicion.views import productos_mostrar, productos_mostrar_descuentos, productos_mostrar_calzado, productos_mostrar_vestidos, productos_mostrar_jeans

urlpatterns = [
    path('productos/',productos_mostrar,name="productos"),
    path('descuentos/',productos_mostrar_descuentos,name="descuentos"),
    path('calzado/',productos_mostrar_calzado,name="calzado"),
    path('vestidos/',productos_mostrar_vestidos,name="vestidos"),
    path('jeans/',productos_mostrar_jeans,name="jeans")
]