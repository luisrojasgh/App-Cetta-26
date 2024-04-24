from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Compra, ItemCompra

admin.site.register(Usuario, UserAdmin)
admin.site.register(Compra)
admin.site.register(ItemCompra)

