from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

# Create your models here.

from django.db import models

class Direccion(models.Model):
    direccion = models.CharField(max_length=254)
    municipio = models.CharField(max_length=100)
    barrio_vereda = models.CharField(max_length=100)
    
    class Meta:
        verbose_name='Dirección'
        verbose_name_plural='Direcciones'

    def __str__(self):
        return f'{self.direccion}, {self.municipio}, {self.barrio_vereda}'


class Usuario(models.Model):
    nombre= models.CharField(max_length=100,verbose_name="Nombre")
    apellidos= models.CharField(max_length=100,verbose_name="Apellidos")
    
    class TipoDocumento(models.TextChoices):
        CEDULA='CC',_("Cédula")
        TARJETA='TI',_("Tarjeta de Identidad")
        CEDULA_EXTRANJERIA='CE',_("Cédula de Extrangería")

    tipo_documento=models.CharField(max_length=2,choices=TipoDocumento.choices,verbose_name="Tipo de Documento")
    documento= models.PositiveIntegerField(verbose_name="Documento", unique=True)
    correo = models.EmailField(max_length=50, verbose_name="Correo", blank=True, null=True)
    celular = models.CharField(max_length=15, blank=True, null=True)
    telefono_fijo = models.CharField(max_length=15, blank=True, null=True)
    password = models.CharField(max_length=128)
    estado=models.BooleanField(default=True)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE, related_name='direccion_usuario')

    @property
    def primer_nombre(self):
        nombre_dividido = self.nombre.split(" ")
        primer_nombre = nombre_dividido[0]
        return primer_nombre

    class Meta:
        verbose_name="Usuario"
        verbose_name_plural="Usuarios"

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"
    