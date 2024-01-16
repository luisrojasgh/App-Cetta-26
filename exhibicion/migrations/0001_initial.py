# Generated by Django 5.0 on 2023-12-31 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=60, verbose_name='Nombre')),
                ('descripcion', models.TextField()),
                ('descuento', models.DecimalField(decimal_places=1, max_digits=2)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('referencia', models.CharField(max_length=50)),
                ('estado', models.BooleanField(default=True)),
                ('categoria', models.CharField(choices=[('CALZADO', 'Calzado'), ('JEANS', 'Jeans'), ('VESTIDOS', 'Vestidos')], default='CALZADO', max_length=20, verbose_name='Categoría')),
                ('talla', models.CharField(choices=[('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('36.5', '36.5'), ('37', '37'), ('38', '38'), ('39', '39'), ('40', '40'), ('40.5', '40.5'), ('41', '41'), ('42', '42')], default='S', max_length=4, verbose_name='Talla')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='productos/')),
            ],
        ),
    ]
