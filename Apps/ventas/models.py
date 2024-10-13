from django.db import models
from Apps.empleados.models import Empleado


class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.nombre}'


class Producto(models.Model):

    descripcion = models.CharField(max_length=100, unique=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_disponible = models.PositiveIntegerField()
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE,related_name='productos')

    def __str__(self):
        return f'{self.descripcion},{self.cantidad_disponible},{self.categoria}'


class Venta(models.Model):

    TIPOS_COMPROBANTE =[
        ('factura A','FACTURA A'),
        ('factura B','FACTURA B'),
        ('factura C','FACTURA C'),
        ('factura M','FACTURA M'),
        ('ticket','TICKET'),
        ('recibo A','RECIBO A'),
        ('recibo B','RECIBO B'),
    ]
    TIPOS_VENTA =[
        ('contado','CONTADO'),
        ('debito','DÉBITO'),
        ('credito','CRÉDITO'),
        ('cuotas','CUOTAS'),
    ]
    TIPOS_PAGO=[
        ('tarjeta de credito','TARJETA DE CRÉDITO'),
        ('tarjeta de debito','TARJETA DE DÉBITO'),
        ('contado','CONTADO'),
    ]
    fecha = models.DateField(auto_now=True)
    nro_comprobante = models.CharField(max_length=10, unique=True)
    comprobante = models.CharField(max_length=10,choices=TIPOS_COMPROBANTE)
    venta = models.CharField(max_length=7,choices=TIPOS_VENTA)
    pago = models.CharField(max_length=18,choices=TIPOS_PAGO)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name='ventas_realizadas')
    producto = models.ManyToManyField(Producto)
    observaciones = models.TextField(blank=True,null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.fecha}{self.nro_comprobante},{self.empleado}'


class Mayorista(models.Model):

    cuil = models.CharField(max_length=10,unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=150)
    rubro = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.nombre},{self.apellido},{self.rubro}'