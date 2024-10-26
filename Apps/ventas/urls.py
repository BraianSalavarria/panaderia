
from django.urls import path
from Apps.ventas.views import (lista_de_categorias, agregar_categoria, eliminar_categoria, editar_categoria,
                               lista_productos, agregar_producto, editar_producto, eliminar_producto, agregar_mayorista,
                               lista_mayoristas, editar_mayorista, eliminar_mayorista,registrar_venta, crear_item_venta,
                               obtener_precio_producto)

app_name = 'ventas'

urlpatterns = [

    path('agregar-categoria',agregar_categoria, name='agregar_categoria'),
    path('lista-categorias',lista_de_categorias,name='lista_categorias'),
    path('eliminar-categoria/<int:id>',eliminar_categoria,name='eliminar_categoria'),
    path('editar-categoria',editar_categoria,name='editar_categoria'),
    path('lista-productos',lista_productos,name="lista_productos"),
    path('agregar-producto',agregar_producto,name='agregar_producto'),
    path('editar-producto',editar_producto,name='editar_producto'),
    path('eliminar-producto/<int:id>',eliminar_producto,name='eliminar_producto'),
    path('agregar-mayorista',agregar_mayorista,name='agregar_mayorista'),
    path('lista-mayorista',lista_mayoristas,name='lista_mayoristas'),
    path('editar-mayorista',editar_mayorista,name='editar_mayorista'),
    path('eliminar-mayorista/<int:id>',eliminar_mayorista,name="eliminar_mayorista"),
    path('registrar-venta',registrar_venta,name='registrar_venta'),
    path('crear-item-venta',crear_item_venta,name='crear_item_venta'),
    path('obtener-precio-producto/', obtener_precio_producto, name='obtener_precio_producto'),
    
]