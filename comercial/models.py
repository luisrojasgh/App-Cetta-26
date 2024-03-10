from django.db import models
from django.utils.translation import gettext_lazy as _
""" from django.contrib.auth.models import User """

# Create your models here.
class User(models.Model):
    pass


class Compra(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    class Estado(models.TextChoices):
        REALIZADA='1',_("Realizada")
        RECHAZADA='0',_("Rechazada")
    estado=models.CharField(max_length=2,choices=Estado.choices,verbose_name="Estado")
    iva = models.IntegerField()
    subtotal = models.IntegerField()

    def calcular_total(self):
        # Calcular el precio con el IVA aplicado.
        total = (self.subtotal)+((self.subtotal*self.iva)/100)
        return total

    def __str__(self):
        return f"Factura de compra # {self.id}"


