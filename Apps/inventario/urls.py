from django.urls import path
from Apps.inventario.views import lista_proveedores,agregar_proveedor, editar_proveedor,eliminar_proveedor

app_name='inventario'

urlpatterns = [
    path('lista-proveedores',lista_proveedores,name='lista_proveedores'),
    path('agregar-proveedor',agregar_proveedor,name='agregar_proveedor'),
    path('editar-proveedor',editar_proveedor,name='editar_proveedor'),
    path('eliminar-proveedor/<int:id>',eliminar_proveedor,name='eliminar_proveedor'),

]