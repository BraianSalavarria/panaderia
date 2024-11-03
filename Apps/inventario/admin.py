from django.contrib import admin
from Apps.inventario.models import Proveedor,Insumo,Pedido,PedidoRecibido

admin.site.register(Proveedor)
admin.site.register(Insumo)
admin.site.register(Pedido)
admin.site.register(PedidoRecibido)
