from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from exhibicion.models import Producto
#from django.db.models import F, Sum, IntegerField
""" from django.contrib.auth.models import User """

# Modelo Usuario, extendido desde la clase abstracta AbstractUser. Sobresescribe el modelo User propio de django.
# e implementa los atributos y métodos del modelo User.
class Usuario(AbstractUser):

    class TipoDocumento(models.TextChoices):
        CEDULA='CC',_("Cédula")
        TARJETA='TI',_("Tarjeta de Identidad")
        CEDULA_EXTRANJERIA='CE',_("Cédula de Extrangería")
    tipo_documento=models.CharField(max_length=2,choices=TipoDocumento.choices,verbose_name="Tipo de Documento")
    documento= models.CharField(max_length=50, verbose_name="Documento", null=True, blank=True,)
    numero_telefono = models.CharField(max_length=20, null=True, blank=True)
    numero_celular = models.CharField(max_length=20, null=False, blank=False)
    direccion = models.CharField(max_length=250, null=False, blank=False)
    municipio = models.CharField(max_length=100, null=False, blank=False)
    barrio_vereda = models.CharField(max_length=100, null=False, blank=False)

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
        ENTREGADA='1',_("Entregada")
        NO_ENTREGADA='0',_("No entregada")
    estado=models.CharField(max_length=2,choices=Estado.choices,verbose_name="Estado",default='0')
    total = models.IntegerField()

    
    def mostrar_datos(self):
        return f"Compra N° {self.id}, con valor de: {self.total}, realizada el: {self.fecha_creacion}. Usuario: {self.usuario.first_name} {self.usuario.last_name} "

    def __str__(self):
        return f"Compra N° {self.id} - Usuario: {self.usuario.username} - Fecha: {self.fecha_creacion} - Total: {self.total}"

class ItemCompra(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)

    def __str__(self):
        return f'Cantidad: {self.cantidad} - Nombre:  {self.producto.nombre} Valor: {self.producto.precio} - {self.fecha_creacion} - Compra N°: {self.compra.id}'
    



