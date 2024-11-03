from django.contrib import admin
from Apps.ventas.models import Categoria,Producto, Mayorista, Venta

admin.site.register(Categoria)
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display=['descripcion','precio','cantidad_disponible','categoria']

admin.site.register(Mayorista)
admin.site.register(Venta)    