from django.db import models

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