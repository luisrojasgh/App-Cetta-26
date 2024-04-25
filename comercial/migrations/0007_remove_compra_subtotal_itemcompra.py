# Generated by Django 5.0 on 2024-04-22 20:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comercial', '0006_alter_compra_iva'),
        ('exhibicion', '0005_alter_producto_categoria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compra',
            name='subtotal',
        ),
        migrations.CreateModel(
            name='ItemCompra',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('cantidad', models.IntegerField(default=1)),
                ('compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comercial.compra')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exhibicion.producto')),
            ],
        ),
    ]