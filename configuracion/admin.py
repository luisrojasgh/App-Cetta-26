from django.contrib import admin

from .models import Slider, DescuentoInformacion, DescuentoImagen, ProductoIndex

# Register your models here.
admin.site.register(Slider)
admin.site.register(DescuentoInformacion)
admin.site.register(DescuentoImagen)
admin.site.register(ProductoIndex)
