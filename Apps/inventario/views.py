from django.contrib.auth.decorators import login_required, permission_required
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.db.models.fields import return_None
from django.db.transaction import commit
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages


from Apps.inventario.forms import ProveedorForm, ItemsPedidosFormSet, ItemsPedidosRecibidoFormSet
from Apps.inventario.models import Proveedor, Insumo, Pedido, ItemPedido, PedidoRecibido, ItemPedidoRecicido
from Apps.ventas.forms import ItemsVentaFormSet
from Apps.ventas.models import Categoria
from Apps.empleados.models import Empleado



#--------------------------------------------- PROVEEDOR ---------------------------------------------------------------------------------
@login_required(login_url='usuario:login')
@permission_required('inventario.view_proveedor', raise_exception=True)
def lista_proveedores(request):
    proveedores = Proveedor.objects.all()
    proveedor_form = ProveedorForm()
    return render(request, 'inventario/administrarProveedores.html',{'form':proveedor_form ,'proveedores':proveedores})



@login_required(login_url='usuario:login')
@permission_required('inventario.add_proveedor', raise_exception=True)
def agregar_proveedor(request):
    if request.method == 'POST':
        proveedor_form = ProveedorForm(request.POST)
        if proveedor_form.is_valid():
            proveedor_form.save()
            messages.success(request,f'Proveedor "{proveedor_form.cleaned_data['nombre']}" Registrado Correctamente')
            return redirect(to='inventario:lista_proveedores')
        else:
            # Si el formulario no es válido, renderiza la página con los errores
            return render(request, 'inventario/administrarProveedores.html', {
                'form': proveedor_form,
                'errors': proveedor_form.errors
            })



@login_required(login_url='usuario:login')
@permission_required('inventario.change_proveedor', raise_exception=True)
def editar_proveedor(request):
    if request.method == 'POST':
        proveedor = get_object_or_404(Proveedor, id = request.POST['id_proveedor'])
        proveedor.nombre = request.POST['nombreProveedorM']
        proveedor.apellido = request.POST['apellidoProveedorM']
        proveedor.empresa = request.POST['empresaM']

        proveedor.save()
        messages.success(request,f'Proveedor "{proveedor.nombre}" Actualizado Correctamente')
        return redirect(to='inventario:lista_proveedores')



@login_required(login_url='usuario:login')
@permission_required('inventario.delete_proveedor', raise_exception=True)
def eliminar_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, id=id)
    proveedor.delete()
    messages.success(request,f'Proveedor "{proveedor.nombre}" Eliminado Exitosamente')
    return  redirect(to='inventario:lista_proveedores')

#---------------------------------------INSUMOS------------------------------------------------------------------
def lista_stock(request):
    stock = Insumo.objects.all()
    proveedores = Proveedor.objects.all()
    return render(request,'inventario/administrarStock.html',{'stock':stock,'proveedores':proveedores})


def agregar_insumo(request):

    if request.method == 'POST':
          try:
                nombre = request.POST['descripcion']
                cantidad = int(request.POST['cantidad'])
                nuevo_insumo = Insumo(nombre=nombre,cantidad=cantidad)
                nuevo_insumo.save()

                proveedores_id =request.POST.getlist('proveedores')
                proveedores = Proveedor.objects.filter(id__in=proveedores_id)
                nuevo_insumo.proveedores.set(proveedores)

                messages.success(request,f'Insumo {nombre} Registrado Correctamente')

          except ValueError:
              messages.error(request, 'Error: vala de cantidad invalido')

    return redirect(to='inventario:stock_disponible')

def editar_proveedor_insumo(request,id):
    if request.method == 'POST':
        insumo = get_object_or_404(Insumo, id = id)
        nuevo_proveedor_id = request.POST.get('nuevo_proveedor')

        if nuevo_proveedor_id:
            nuevo_proveedor = get_object_or_404(Proveedor, id=nuevo_proveedor_id)
            insumo.proveedores.add(nuevo_proveedor)
            messages.success(request,'Proveedor Asignado Correctamente')
        return redirect(to='inventario:stock_disponible')


def eliminar_proveedor_insumo(request,id):
        if request.method == 'POST':
            insumo = get_object_or_404(Insumo, id = id)
            proveedor_a_eliminar_id = request.POST.get('proveedor_a_eliminar')

            if proveedor_a_eliminar_id:
                proveedor_a_eliminar = get_object_or_404(Proveedor, id=proveedor_a_eliminar_id)
                insumo.proveedores.remove(proveedor_a_eliminar)
                messages.success(request,f'Proveedor "{proveedor_a_eliminar.nombre}" Eliminado Correctamente')
            return redirect('inventario:stock_disponible')

def editar_insumo(request):
    if request.method == 'POST':
        id_insumo = request.POST['id_insumo']
        insumo = get_object_or_404(Insumo,id = id_insumo)
        nombre = request.POST['descripcionM']
        cantidad = int(request.POST['cantidadM'])

        insumo.nombre=nombre
        insumo.cantidad=cantidad

        insumo.save()
        messages.success(request,f'Insumo "{nombre}" Actualizado Correctamente')

        return redirect(to='inventario:stock_disponible')

def eliminar_insumo(request,id):
    insumo = get_object_or_404(Insumo, id=id)
    if insumo:
        insumo.delete()
        messages.success(request,f'Insumo "{insumo.nombre}" Eliminado Correctamente')
    else:
        messages.error(request,f'Error: No se Pudo Eliminar Insumo 2{insumo.nombre}"')

    return redirect(to='inventario:stock_disponible')

#---------------------------------------- Pedidos--------------------------------------------------------------------
def registrar_pedido(request):
    proveedores = Proveedor.objects.all()
    formset = ItemsPedidosFormSet()
    return render(request,'inventario/realizarPedido.html',{'proveedores':proveedores,'formset':formset})



def obtener_insumos_proveedor(request,id):
    if request.method == 'GET':
        get_object_or_404(Proveedor,id=id)
        insumos = Insumo.objects.filter(proveedores__id = id).values('id','nombre','cantidad')

    return JsonResponse(list(insumos), safe=False)


from django.contrib import messages

def crear_item_pedido(request):
    if request.method == 'POST':
        # Obtenemos el ID del proveedor desde el formulario
        proveedor_id = request.POST['proveedor-select']
        nro_pedido = request.POST['nro_pedido']
        observaciones = request.POST['observaciones']

        # Obtenemos la instancia de Proveedor
        proveedor = Proveedor.objects.get(id=proveedor_id)

        # Obtenemos el usuario actual y luego el empleado asociado
        usuario = request.user
        empleado = Empleado.objects.get(usuario=usuario)

        # Creamos el pedido con los datos obtenidos
        nuevo_pedido = Pedido(
            nro_pedido=nro_pedido,
            observaciones=observaciones,
            proveedor=proveedor,
            empleado=empleado
        )
        nuevo_pedido.save()

        # Inicializamos el formset con los datos POST
        formset = ItemsPedidosFormSet(request.POST, instance=nuevo_pedido)

        # Validamos el formset antes de acceder a los datos limpios
        if formset.is_valid():
            has_error = False  # Variable para rastrear errores

            for item_form in formset:
                insumo = item_form.cleaned_data.get('insumo')
                cantidad = item_form.cleaned_data.get('cantidad')

                # Verificamos si la cantidad es 0 y añadimos un error específico
                if insumo and cantidad is not None:
                    if cantidad == 0:
                        item_form.add_error('cantidad', 'La cantidad no puede ser 0.')
                        has_error = True
                    else:
                        # Guarda cada item del formset con el pedido asociado
                        item = item_form.save(commit=False)
                        item.pedido = nuevo_pedido
                        item.save()

                        # Actualizamos la cantidad de cada insumo (es un insumo, no deberia actualizar el stock)
                        #insumo.cantidad += cantidad
                        #insumo.save()

            # Si no hay errores específicos, guardamos el pedido
            if not has_error:

                messages.success(request, f'Pedido Nro: "{nro_pedido}" Registrado Correctamente')
                return redirect(to='inventario:registrar_pedido')
            else:
                messages.error(request, 'Error: La cantidad no puede ser Cero.')

        else:
            messages.error(request, 'Error: Seleccione el Insumo')

        # Si el formset no es válido, renderizamos la misma plantilla con el formset y errores
        proveedores = Proveedor.objects.all()
        return render(request, 'inventario/realizarPedido.html', {'proveedores': proveedores, 'formset': formset})

    else:
        # Si es una solicitud GET, mostramos un formset vacío
        proveedores = Proveedor.objects.all()
        formset = ItemsPedidosFormSet()
        return render(request, 'inventario/realizarPedido.html', {'proveedores': proveedores, 'formset': formset})


def lista_pedidos(request):
    pedidos = Pedido.objects.filter(estado=False)
    provedores = Proveedor.objects.all()
    formset = ItemsPedidosRecibidoFormSet()
    return render(request,'inventario/controlarPedido.html',{'pedidos':pedidos, 'proveedores':provedores,'formset':formset})

def detalles_pedido(request, id):
    pedido = get_object_or_404(Pedido, id = id)
    items = ItemPedido.objects.filter(pedido=pedido).values('insumo__nombre', 'cantidad')
    data = {
        'nro_pedido': pedido.nro_pedido,
        'fecha': pedido.fecha,
        'observaciones': pedido.observaciones,
        'proveedor': f'{pedido.proveedor.nombre}  {pedido.proveedor.apellido} - {pedido.proveedor.empresa}',
        'items': list(items)
    }
    return JsonResponse(data)

def crear_item_pedido_recibido(request):
    if request.method == 'POST':
        try:
            # Obtenemos los datos del pedido y lo guardamos
            nro_comprobante = request.POST['nro_comprobante']
            nro_pedido = request.POST['nro_pedidoRealizado']
            observaciones = request.POST['observaciones']
            proveedor = get_object_or_404(Proveedor, id=request.POST['proveedor-select'])
            conformidad = request.POST.get('conformidad') == 'on'
            total = request.POST['totalFactura']

            # Obtenemos el empleado logueado
            usuario = request.user
            empleado = Empleado.objects.get(usuario=usuario)

            nuevo_pedido_recibido = PedidoRecibido(
                nro_comprobante=nro_comprobante,
                nro_pedido=nro_pedido,
                observaciones=observaciones,
                conformidad=conformidad,
                proveedor=proveedor,
                empleado=empleado,
                total=total
            )

            nuevo_pedido_recibido.save()

            #obtenemos el pedido hecho para darlo como controlado
            pedido_echo = Pedido.objects.get(nro_pedido=request.POST['nro_pedidoRealizado'])
            pedido_echo.estado = True
            pedido_echo.save()

            # Trabajamos con los formsets
            formset = ItemsPedidosRecibidoFormSet(request.POST, instance=nuevo_pedido_recibido)

            # Validamos el formset
            if formset.is_valid():
                has_error = False  # Variable para rastrear errores

                for item_form in formset:
                    insumo = item_form.cleaned_data.get('insumo')
                    cantidad = item_form.cleaned_data.get('cantidad')

                    # Verificamos si la cantidad es 0 y añadimos un error específico
                    if insumo and cantidad is not None:
                        if cantidad == 0:
                            item_form.add_error('cantidad', 'La cantidad no puede ser 0.')
                            has_error = True
                        else:
                            # Guarda cada item del formset con el pedido asociado
                            item = item_form.save(commit=False)
                            item.pedido = nuevo_pedido_recibido
                            item.save()
                            # Actualizamos la cantidad de cada insumo
                            insumo.cantidad += cantidad
                            insumo.save()

                if not has_error:
                    messages.success(request, f'Pedido Ingresado Nro "{nro_comprobante}" Registrado Correctamente')

        except IntegrityError:
            messages.error(request, f'Error: Ya se registró un Ingreso con el Nro de Pedido "{nro_pedido}"')
        except ValidationError:
            messages.error(request, 'Error: Datos Ingresados Inválidos')

    return redirect(to='inventario:lista_pedidos')


def todos_los_pedidos(request):
    pedidos = Pedido.objects.filter(estado=True)
    pedidos_recibidos = PedidoRecibido.objects.all()

    return render(request,'inventario/todosLosPedidos.html',{'pedidos':pedidos,'pedidos_recibidos':pedidos_recibidos})


def eliminar_pedido(request,id):
    if request.method == 'GET':
        pedido = get_object_or_404(Pedido,id=id)
        pedido.delete()
        messages.success(request,f'Pedido Nro: "{pedido.nro_pedido}" Eliminado Correctamene')
        return redirect(to='inventario:todos_los_pedidos')


def detalles_pedido_recibido(request, id):
    pedido_recibido = get_object_or_404(PedidoRecibido, id = id)
    items = ItemPedidoRecicido.objects.filter(pedido_recibido=pedido_recibido).values('insumo__nombre', 'cantidad','precio_unit','total')
    data = {
        'nro_comprobante':pedido_recibido.nro_comprobante,
        'nro_pedido': pedido_recibido.nro_pedido,
        'fecha': pedido_recibido.fecha,
        'conformidad':pedido_recibido.conformidad,
        'total':pedido_recibido.total,
        'observaciones': pedido_recibido.observaciones,
        'proveedor': f'{pedido_recibido.proveedor.nombre}  {pedido_recibido.proveedor.apellido} - {pedido_recibido.proveedor.empresa}',
        'items': list(items)
    }
    return JsonResponse(data)

def eliminar_pedido_recibido(request,id):
    if request.method == 'GET':
        pedido_recibido = get_object_or_404(PedidoRecibido,id=id)
        items_pedido_recibido = ItemPedidoRecicido.objects.filter(pedido_recibido=pedido_recibido)

        for item in items_pedido_recibido:
            insumo = Insumo.objects.get(id = item.insumo.id)
            insumo.cantidad -= item.cantidad
            insumo.save()

        pedido_recibido.delete()

        messages.success(request,f'Pedido Ingresado Nro: "{pedido_recibido.nro_comprobante}" Eliminado Correctamene')
        return redirect(to='inventario:todos_los_pedidos')









