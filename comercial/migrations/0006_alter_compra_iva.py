# Generated by Django 5.0 on 2024-04-22 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comercial', '0005_alter_compra_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='iva',
            field=models.IntegerField(default=19),
        ),
    ]