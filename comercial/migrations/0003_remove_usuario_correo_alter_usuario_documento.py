# Generated by Django 5.0 on 2024-03-14 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comercial', '0002_alter_usuario_documento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='correo',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='documento',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Documento'),
        ),
    ]
