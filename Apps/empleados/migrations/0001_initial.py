# Generated by Django 5.1.1 on 2024-10-08 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuit', models.CharField(max_length=11, unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=150)),
                ('telefono_fijo', models.CharField(blank=True, max_length=20, null=True)),
                ('telefono_celular', models.CharField(max_length=20)),
                ('calle', models.CharField(max_length=200)),
                ('nro_calle', models.PositiveIntegerField()),
                ('localidad', models.CharField(max_length=200)),
                ('dpto', models.CharField(max_length=200)),
                ('fecha_nacimiento', models.DateField()),
                ('fecha_ingreso', models.DateField()),
            ],
        ),
    ]