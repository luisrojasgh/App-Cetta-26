from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
""" from django.contrib.auth.models import User """

# Create your models here.
class Usuario(AbstractUser):

    class TipoDocumento(models.TextChoices):
        CEDULA='CC',_("Cédula")
        TARJETA='TI',_("Tarjeta de Identidad")
        CEDULA_EXTRANJERIA='CE',_("Cédula de Extrangería")
    tipo_documento=models.CharField(max_length=2,choices=TipoDocumento.choices,verbose_name="Tipo de Documento")
    documento= models.PositiveIntegerField(verbose_name="Documento", unique=True)
    email = models.EmailField(blank=False)
    numero_telefono = models.CharField(max_length=20, null=True, blank=True)
    numero_celular = models.CharField(max_length=20, null=False, blank=False)
    direccion = models.CharField(max_length=250, null=False, blank=False)
    municipio = models.CharField(max_length=100, null=False, blank=False)
    barrio_vereda = models.CharField(max_length=100, null=False, blank=False)
    estado=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural="Usuarios"

    @property
    def get_nombre_completo(self):
        return '{} {}'.format(self.first_name.title(), self.last_name.title())
    
    @property
    def get_primer_nombre(self):
        return '{}'.format(self.first_name.title())
    
    
    def usuario_activo(self):
        if self.estado:
            return Usuario.objects.filter(usuario=self, estado=True)
        else:
            return Usuario.objects.none()
    
    def direccion_completa(self):
    
        partes = [self.direccion, self.barrio_vereda, self.municipio]
        direccion_completa = ', '.join(parte for parte in partes if parte)
        
        return direccion_completa or 'No disponible'
    
    def clean(self):
        self.first_name= self.first_name.title()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Compra(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=False, blank=False)
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


