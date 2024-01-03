
from django.urls import path
from exhibicion.views import productos_mostrar

urlpatterns = [
    path('productos/',productos_mostrar,name="productos"),
]