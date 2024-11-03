from tkinter.font import names

from django.urls import path
from Apps.inventario.views import (lista_proveedores, agregar_proveedor, editar_proveedor, eliminar_proveedor,
                                   lista_stock, agregar_insumo, eliminar_proveedor_insumo, editar_proveedor_insumo, editar_insumo,
                                   eliminar_insumo,registrar_pedido, obtener_insumos_proveedor,crear_item_pedido, lista_pedidos,detalles_pedido,
                                   crear_item_pedido_recibido,todos_los_pedidos,eliminar_pedido,detalles_pedido_recibido,eliminar_pedido_recibido)

app_name='inventario'

urlpatterns = [
    path('lista-proveedores',lista_proveedores,name='lista_proveedores'),
    path('agregar-proveedor',agregar_proveedor,name='agregar_proveedor'),
    path('editar-proveedor',editar_proveedor,name='editar_proveedor'),
    path('eliminar-proveedor/<int:id>',eliminar_proveedor,name='eliminar_proveedor'),
    path('lista-stock',lista_stock,name='stock_disponible'),
    path('agregar-insumo',agregar_insumo,name='agregar_insumo'),
    path('editar-proveedor-insumo/<int:id>',editar_proveedor_insumo,name='editar_proveedor_insumo'),
    path('elimianr-proveedor-insumo/<int:id>',eliminar_proveedor_insumo,name='eliminar_proveedor_insumo'),
    path('editar-insumo',editar_insumo,name='editar_insumo'),
    path('eliminar-insumo/<int:id>',eliminar_insumo,name='eliminar_insumo'),
    path('registrar-pedido',registrar_pedido,name='registrar_pedido'),
    path('obtener-insumos-proveedor/<int:id>',obtener_insumos_proveedor,name='obtener_insumos_proveedor'),
    path('crear-item-pedido',crear_item_pedido,name='crear_item_pedido'),
    path('lista-pedidos',lista_pedidos,name='lista_pedidos'),
    path('detalles-pedido/<int:id>',detalles_pedido,name='detalles_pedido'),
    path('crear-item-pedido-recibido',crear_item_pedido_recibido,name='crear_item_pedido_recibido'),
    path('todos-los-pedidos',todos_los_pedidos,name='todos_los_pedidos'),
    path('eliminar-pedido/<int:id>',eliminar_pedido,name='eliminar_pedido'),
    path('detalles-pedidos-recibidos/<int:id>',detalles_pedido_recibido,name='detalles_pedido_recibido'),
    path('eliminar-pedido-recibido/<int:id>',eliminar_pedido_recibido,name='eliminar_pedido_recibido'),


]