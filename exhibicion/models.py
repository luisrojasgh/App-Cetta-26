from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Producto(models.Model):
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
    descuento = models.DecimalField(max_digits=2, decimal_places=1)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    referencia = models.CharField(max_length=50)
    estado = models.BooleanField(default=True)
    categoria = models.CharField(max_length=20, choices=Categoria.choices, verbose_name="Categoría", default=Categoria.CALZADO)
    talla = models.CharField(max_length=4, choices=Talla.choices, verbose_name="Talla", default=Talla.TALLA_S)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)

    class Meta:
        verbose_name='producto'
        verbose_name_plural='productos'

    def __str__(self):
        return self.nombre
    