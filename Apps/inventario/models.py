from django.db import models
from Apps.empleados.models import Empleado


class Proveedor(models.Model):

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=150)
    empresa = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.nombre} - {self.apellido} - {self.empresa}'


class Insumo (models.Model):

    nombre = models.CharField(max_length=100)
    proveedores = models.ManyToManyField(Proveedor,related_name='insumos')
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.nombre},{self.cantidad}'


class Pedido (models.Model):

    nro_pedido = models.CharField(max_length=20, unique=True)
    fecha = models.DateField(auto_now_add=True)
    proveedor = models.ManyToManyField(Proveedor)
    observaciones =  models.TextField(blank=True, null=True)


    def __str__(self):
        return f'{self.nro_pedido},{self.fecha}'


class PedidoRecibido (models.Model):

    fecha = models.DateField(auto_now_add=True)
    nro_comprobante = models.CharField(max_length=10, unique=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    conformidad = models.BooleanField(default=True)
    observaciones = models.TextField(blank=True,null=True)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name='pedidos_recibidos')
    proveedor = models.ManyToManyField(Proveedor)

    def __str__(self):
        return f'{self.nro_comprobante},{self.fecha},{self.proveedor}'


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido,on_delete=models.CASCADE,related_name='items')
    insumo = models.ForeignKey(Insumo, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

class ItemPedidoRecicido(models.Model):
    pedido_recivido = models.ForeignKey(PedidoRecibido, on_delete=models.CASCADE,related_name='items')
    insumo = models.ForeignKey(Insumo, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()