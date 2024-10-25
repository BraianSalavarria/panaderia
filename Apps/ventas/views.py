from decimal import Decimal

from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils.datastructures import MultiValueDictKeyError

from Apps.ventas.forms import ItemsVentaFormSet, VentaForm
from Apps.ventas.models import Categoria, Producto, Mayorista


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
      except MultiValueDictKeyError:
          messages.error(request,'Error: Debe Seleccionar o Registrar Previamente una Categoria de Productos')

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


def lista_mayoristas(request):

    mayoristas = Mayorista.objects.all()
    return render(request,'ventas/administrarMayoristas.html',{'mayoristas':mayoristas})


def agregar_mayorista(request):

    if request.method == 'POST':
        try:
                cuil = request.POST['cuilMayorista']
                nombre = request.POST['nombreMayorista']
                apellido = request.POST['apellidoMayorista']
                informacion = request.POST['informacionMayorista']
                mayorista = Mayorista(cuil=cuil, nombre=nombre,apellido=apellido, rubro=informacion)
                mayorista.save()
                messages.success(request, f'El Cliente "{nombre}" se ha Registrado Correctamente')

        except IntegrityError:
            messages.error(request,f'El Cliente "{nombre}" ya se Encuentra Registrado')

    return redirect(to='ventas:lista_mayoristas')

def editar_mayorista(request):

    if request.method == 'POST':

        mayorista = get_object_or_404(Mayorista,id = request.POST['id_mayorista'])

        nombre =  request.POST['nombreMayoristaM']
        apellido =  request.POST['apellidoMayoristaM']
        informacion =  request.POST['informacionMayoristaM']
        cuil = request.POST['cuilMayoristaM']

        mayorista.nombre = nombre
        mayorista.apellido = apellido
        mayorista.rubro = informacion
        mayorista.cuil = cuil

        mayorista.save()
        messages.success(request,f'El Cliente "{nombre}" se ha Actualizado Correctamente ')

    return redirect(to='ventas:lista_mayoristas')


def eliminar_mayorista (request, id):
    mayorista = get_object_or_404(Mayorista,id = id)
    mayorista.delete()
    messages.success(request,f'El Cliente "{mayorista.nombre}" se ha Eliminado Correctamente')
    return redirect(to='ventas:lista_mayoristas')


def registrar_venta(request):
    categorias = Categoria.objects.all()
    venta_form = VentaForm()
    formset = ItemsVentaFormSet()

    return render(request,'ventas/administrarVentas.html',{'categorias':categorias,'form':venta_form,'formset':formset})


def obtener_productos(request):
    categoria_id = request.GET.get('categoria')
    productos = Producto.objects.filter(categoria_id=categoria_id)  # Filtrar los productos por categoría

    # Crear una lista de productos para enviar en la respuesta
    productos_data = [{'id': producto.id, 'nombre': producto.descripcion} for producto in productos]
    return JsonResponse({'productos': productos_data})

def obtener_producto(request, producto_id):
    producto = Producto.objects.get(id = producto_id)

    data = {
        'id':producto.id,
        'descripcion': producto.descripcion,
        'precio': producto.precio,
    }

    return JsonResponse({'producto':data}, status = 200)


from django.shortcuts import render, redirect
from django.contrib import messages


def crear_item_venta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        formset = ItemsVentaFormSet(request.POST)

        if form.is_valid() and formset.is_valid():
            venta = form.save(commit=False)
            total = 0
            has_stock_error = False  # Variable para verificar si hay errores de stock

            for item_form in formset:
                producto = item_form.cleaned_data.get('producto')
                cantidad = item_form.cleaned_data.get('cantidad')

                if producto and cantidad:
                    # Comprobamos si hay suficiente stock
                    if producto.cantidad_disponible < cantidad:
                        item_form.add_error('cantidad',f'Solo hay {producto.cantidad_disponible} unidades disponibles de {producto.descripcion}.')
                        has_stock_error = True
                    else:
                        total += producto.precio * cantidad

            if has_stock_error:
                messages.error(request, 'Error: No se puede completar la venta debido a falta de stock.')
            else:
                # Guardamos los cambios si no hay errores de stock
                venta.total = total
                venta.save()
                formset.instance = venta  # Asignamos la instancia de venta al formset
                formset.save()

                # Actualizamos el stock de cada producto
                for item_form in formset:
                    producto = item_form.cleaned_data.get('producto')
                    cantidad = item_form.cleaned_data.get('cantidad')
                    if producto and cantidad:
                        producto.cantidad_disponible -= cantidad
                        producto.save()

                messages.success(request, 'Venta Registrada con Éxito')
                return redirect('ventas:registrar_venta')
        else:
            messages.error(request, 'Error en la venta')

    else:
        form = VentaForm()
        formset = ItemsVentaFormSet()

    return render(request, 'ventas/administrarVentas.html', {'form': form, 'formset': formset})




