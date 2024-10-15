from decimal import Decimal
from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from Apps.ventas.models import Categoria, Producto


def lista_de_categorias(request):
    categorias = Categoria.objects.all()
    return render(request,'ventas/administrarCategorias.html',{'categorias':categorias})

def agregar_categoria(request):

    if request.method == 'POST':
        try:
            nombre = request.POST['descripcionProducto']
            nueva_categoria = Categoria(nombre=nombre)
            nueva_categoria.save()

            messages.success(request,f'Categoria "{nombre}" Agregada Exitosamente')

        except IntegrityError:
            messages.error(request,f'La Categoria "{nombre}" ya Existe')

    return redirect(to='ventas:lista_categorias')

def eliminar_categoria(request, id):

        categoria_eliminada = get_object_or_404(Categoria,id=id)
        categoria_eliminada.delete()
        messages.success(request,f'Categoria "{categoria_eliminada.nombre}" Eliminada Exitosamente')

        return redirect(to='ventas:lista_categorias')

def editar_categoria(request):

    if request.method == 'POST':
        id = request.POST['categoria_id']
        nuevo_nombre = request.POST['categoria_nombre']
        categoria_modificada = get_object_or_404(Categoria,id=id)
        categoria_modificada.nombre = nuevo_nombre
        categoria_modificada.save()
        messages.success(request,f'Categoria "{nuevo_nombre}" Modificada Exitosamente')

        return redirect(to='ventas:lista_categorias')



def lista_productos(request):
    productos = Producto.objects.all()
    categorias = Categoria.objects.all()
    return render(request,'ventas/administrarProductos.html',{'productos':productos, 'categorias':categorias})


def agregar_producto(request):

    if request.method == 'POST':
      try:
            id_categoria = request.POST['categoriaProducto']
            categoria = get_object_or_404(Categoria,id =id_categoria)

            descripcion = request.POST['descripcionProducto']
            precio = Decimal(request.POST['precioProducto'])
            cantidad = int(request.POST['cantidadProducto'])

            nuevo_producto = Producto(descripcion=descripcion,precio=precio,cantidad_disponible=cantidad,categoria=categoria)
            nuevo_producto.save()
            messages.success(request, f'Producto "{descripcion}" Registrado Correctamente')

      except ValueError:
          messages.error(request,'Error: valor del precio invalido')
      except IntegrityError:
          messages.error(request,f'El Producto "{descripcion}" ya se encuentra registrado')

    return redirect(to='ventas:lista_productos')

def editar_producto(request):

    if request.method == 'POST':
       try:
            categoria = get_object_or_404(Categoria,id = request.POST['categoriaProductoM'])
            descripcion = request.POST['descripcionProductoM']
            precio = Decimal(request.POST['precioProductoM'])
            cantidad = int(request.POST['cantidadProductoM'])

            producto_actualizado = get_object_or_404(Producto,id=request.POST['id_producto'])
            producto_actualizado.descripcion = descripcion
            producto_actualizado.precio = precio
            producto_actualizado.cantidad_disponible = cantidad
            producto_actualizado.categoria = categoria
            producto_actualizado.save()
            messages.success(request,f'El Producto "{producto_actualizado.descripcion}" se ha Actualizado Correctamente')


       except ValueError:
                messages.error(request,'Error: valor del precio invalido')

    return redirect(to='ventas:lista_productos')

def eliminar_producto(request,id):
    producto = get_object_or_404(Producto,id = id)
    producto.delete()
    messages.success(request,f'El Producto "{producto.descripcion}" se ha Eliminado Correctamente')
    return redirect(to='ventas:lista_productos')