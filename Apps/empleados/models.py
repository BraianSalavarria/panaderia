from django.db import models

class Empleado(models.Model):
    cuil = models.CharField(max_length=12, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=150)
    telefono_fijo = models.CharField(max_length=20,blank=True,null=True)
    telefono_celular = models.CharField(max_length=20)
    calle = models.CharField(max_length=200)
    nro_calle = models.PositiveIntegerField()
    localidad = models.CharField(max_length=200)
    dpto = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField(blank=False,null=False)
    fecha_ingreso = models.DateField(blank=False,null=False)

    def __str__(self):
        return f'{ {self.nombre},{self.apellido} }'
