# Generated by Django 5.1.1 on 2024-10-22 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0004_remove_venta_empleado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='nro_comprobante',
            field=models.PositiveIntegerField(max_length=10, unique=True),
        ),
    ]
