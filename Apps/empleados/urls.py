from tkinter.font import names

from django.urls import path
from Apps.empleados.views import lista_empleados,editar_empleado,eliminar_empleado,agregar_empleado

app_name='empleados'

urlpatterns= [
    path('lista-empleados',lista_empleados,name='lista_empleados'),
    path('agregar-empleado',agregar_empleado,name='agregar_empleado'),
    path('editar-empleados',editar_empleado, name='editar_empleado'),
    path('eliminar-empleado/<int:id>',eliminar_empleado,name='eliminar_empleado'),

]