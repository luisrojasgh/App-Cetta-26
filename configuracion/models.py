from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Slider(models.Model):
    nombre= models.CharField(max_length=45,verbose_name="Nombre")
    # descripcion= models.CharField(max_length=200,verbose_name="Descripción",blank=True, null=True)
    #url= models.CharField(max_length=100,verbose_name="URL", blank=True, null=True)
    imagen = models.ImageField(upload_to='slider_images/')
    #prioridad = models.PositiveIntegerField(verbose_name="Prioridad")
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class DescuentoInformacion(models.Model):
    nombre= models.CharField(max_length=45,verbose_name="Nombre")
    descripcion= models.CharField(max_length=200,verbose_name="Descripción",blank=True, null=True)
    imagen = models.ImageField(upload_to='descuentos_images/')
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class DescuentoImagen(models.Model):
    nombre= models.CharField(max_length=45,verbose_name="Nombre")
    imagen = models.ImageField(upload_to='Img-descuentos_images/')
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class ProductoIndex(models.Model):
    class Categoria(models.TextChoices):
        CALZADO = 'CALZADO', _('Calzado')
        JEANS = 'JEANS', _('Jeans')
        VESTIDOS = 'VESTIDOS', _('Vestidos')

    class Talla(models.TextChoices):
        TALLA_S = 'S', 'S'
        TALLA_M = 'M', 'M'
        TALLA_L = 'L', 'L'
        TALLA_XL = 'XL', 'XL'
        TRENTAISEIS_Y_MEDIO = '36.5', '36.5'
        TRENTAISIETE = '37', '37'
        TRENTAIOCHO = '38', '38'
        TRENTAINUEVE = '39', '39'
        CUARENTA = '40', '40'
        CUARENTA_Y_MEDIO = '40.5', '40.5'
        CUARENTAIUNO = '41', '41'
        CUARENTAIDOS = '42', '42'

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=60, verbose_name="Nombre")
    descripcion = models.TextField()
    descuento = models.DecimalField(max_digits=3, decimal_places=1)
    precio = models.DecimalField(max_digits=10, decimal_places=1)
    referencia = models.CharField(max_length=50)
    estado = models.BooleanField(default=True)
    categoria = models.CharField(max_length=20, choices=Categoria.choices, verbose_name="Categoría", default=Categoria.CALZADO)
    talla = models.CharField(max_length=4, choices=Talla.choices, verbose_name="Talla", default=Talla.TALLA_S)
    imagen = models.ImageField(upload_to='productos_index/', null=True, blank=True)

    def precio_con_descuento(self):
        # Calcular el precio con el descuento aplicado
        if self.descuento > 0:
            precio_total = (self.precio)-((self.precio*self.descuento)/100)
        else:
            precio_total = self.precio
        return precio_total

    
    def __str__(self):
        return self.nombre