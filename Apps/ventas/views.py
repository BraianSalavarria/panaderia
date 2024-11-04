from decimal import Decimal
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Count
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import IntegrityError
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.datastructures import MultiValueDictKeyError
from reportlab.pdfgen import canvas
from Apps.ventas.forms import ItemsVentaFormSet, VentaForm
from Apps.ventas.models import Categoria, Producto, Mayorista, Venta, ItemVenta
from ..empleados.models import Empleado


#---------------------------------Categorias----------------------------------------------------------------------



@login_required(login_url='usuario:login')
@permission_required('ventas.view_categoria', raise_exception=True)
def lista_de_categorias(request):
    categorias = Categoria.objects.all()
    return render(request,'ventas/administrarCategorias.html',{'categorias':categorias})



@login_required(login_url='usuario:login')
@permission_required('ventas.add_categoria', raise_exception=True)
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



@login_required(login_url='usuario:login')
@permission_required('ventas.delete_categoria', raise_exception=True)
def eliminar_categoria(request, id):

        categoria_eliminada = get_object_or_404(Categoria,id=id)
        categoria_eliminada.delete()
        messages.success(request,f'Categoria "{categoria_eliminada.nombre}" Eliminada Exitosamente')

        return redirect(to='ventas:lista_categorias')


@login_required(login_url='usuario:login')
@permission_required('ventas.change_categoria', raise_exception=True)
def editar_categoria(request):

    if request.method == 'POST':
        id = request.POST['categoria_id']
        nuevo_nombre = request.POST['categoria_nombre']
        categoria_modificada = get_object_or_404(Categoria,id=id)
        categoria_modificada.nombre = nuevo_nombre
        categoria_modificada.save()
        messages.success(request,f'Categoria "{nuevo_nombre}" Modificada Exitosamente')

        return redirect(to='ventas:lista_categorias')

#------------------------------------------- PRODUCTOS ---------------------------------------------------------------------------

@login_required(login_url='usuario:login')
@permission_required('ventas.view_producto', raise_exception=True)
def lista_productos(request):
    productos = Producto.objects.all()
    categorias = Categoria.objects.all()
    return render(request,'ventas/administrarProductos.html',{'productos':productos, 'categorias':categorias})

@login_required(login_url='usuario:login')
@permission_required('ventas.add_producto', raise_exception=True)
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



@login_required(login_url='usuario:login')
@permission_required('ventas.change_producto', raise_exception=True)

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


@login_required(login_url='usuario:login')
@permission_required('ventas.delete_producto', raise_exception=True)
def eliminar_producto(request,id):
    producto = get_object_or_404(Producto,id = id)
    producto.delete()
    messages.success(request,f'El Producto "{producto.descripcion}" se ha Eliminado Correctamente')
    return redirect(to='ventas:lista_productos')


#------------------------------------------ MAYORISTAS
@login_required(login_url='usuario:login')
@permission_required('ventas.view_mayorista', raise_exception=True)
def lista_mayoristas(request):

    mayoristas = Mayorista.objects.all()
    return render(request,'ventas/administrarMayoristas.html',{'mayoristas':mayoristas})



@login_required(login_url='usuario:login')
@permission_required('ventas.add_mayorista', raise_exception=True)
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



@login_required(login_url='usuario:login')
@permission_required('ventas.change_mayorista', raise_exception=True)
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



@login_required(login_url='usuario:login')
@permission_required('ventas.delete_mayorista', raise_exception=True)
def eliminar_mayorista (request, id):
    mayorista = get_object_or_404(Mayorista,id = id)
    mayorista.delete()
    messages.success(request,f'El Cliente "{mayorista.nombre}" se ha Eliminado Correctamente')
    return redirect(to='ventas:lista_mayoristas')


#------------------------------------------------- VENTAS -----------------------------------------------------------
@login_required(login_url='usuario:login')
@permission_required('ventas.view_venta', raise_exception=True)
def registrar_venta(request):
    categorias = Categoria.objects.all()
    venta_form = VentaForm()
    formset = ItemsVentaFormSet()

    return render(request,'ventas/administrarVentas.html',{'categorias':categorias,'form':venta_form,'formset':formset})


@login_required(login_url='usuario:login')
@permission_required('ventas.add_venta', raise_exception=True)
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

                #obtenemos al empleado
                usuario = request.user
                empleado= Empleado.objects.get(usuario=usuario)
                venta.empleado=empleado

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


# views.py
from django.http import JsonResponse
from .models import Producto  # Asegúrate de tener un modelo Producto que contenga los precios


#funcionabilidad extra
def obtener_precio_producto(request):
    producto_id = request.GET.get('producto_id')
    if producto_id:
        try:
            producto = Producto.objects.get(id=producto_id)
            precio = producto.precio  # Asumiendo que el modelo Producto tiene un campo 'precio'
            return JsonResponse({'precio': precio}, status=200)
        except Producto.DoesNotExist:
            return JsonResponse({'error': 'Producto no encontrado'}, status=404)
    return JsonResponse({'error': 'ID de producto no proporcionado'}, status=400)

def lista_ventas(request):
    ventas = Venta.objects.all()
    return render(request,'ventas/ventasRealizadas.html',{'ventas':ventas})


from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Table, TableStyle
from django.conf import settings
import os
from reportlab.lib.utils import ImageReader


def imprimir_venta(request, id):

    #obtenemos la venta y sus detalles
    venta = get_object_or_404(Venta,id=id)
    items_de_venta = ItemVenta.objects.filter(venta = venta)

    #configuracion del archivo de respuesta
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="factura_{venta.nro_comprobante}_{venta.fecha}.pdf"'

    #creamos un objeto canvas para dibujar en el pdf
    c = canvas.Canvas(response, pagesize=A4)
    ancho, alto = A4

    #ruta del logo
    logo_path = os.path.join(settings.BASE_DIR,'static/assets/images/logo.png')

    #insertamos logo
    if os.path.exists(logo_path):
        logo = ImageReader(logo_path)
        c.drawImage(logo,10, alto - 80, width=100, height=50, preserveAspectRatio=True, mask='auto')

        #datos de la panaderia
        nompre_panaderia = 'Panaderia El Maná'
        direccion_panaderia = 'Dirección: Av Virgen del Valle 355 - Catamarca'
        correo_panaderia = 'Correo: panaderiamana@gmail.com'
        telefono_panaderia = 'Tel: 3832415161'
        web_panaderia = 'Sitio Web: www.panaderiamana.com'

        #Datos de la factura
        tipo_comprobante = venta.comprobante_tipo
        nro_comprobante = venta.nro_comprobante
        fecha_factura = venta.fecha
        tipo_venta = venta.venta_tipo
        tipo_pago = venta.pago_tipo

        #Encabezado centrado de la panaderia
        c.setFont("Helvetica-Bold", 20)
        titulo_ancho = c.stringWidth(nompre_panaderia, "Helvetica-Bold", 20 )
        c.drawString((ancho - titulo_ancho) / 2, alto - 50, nompre_panaderia)

        #agregar tipo de comprobante centrado debajo del titulo de la factura
        c.setFont("Helvetica-Bold", 14)
        comprobante_ancho = c.stringWidth(tipo_comprobante, "Helvetica-Bold", 14)
        c.drawString((ancho - comprobante_ancho) / 2, alto - 80, tipo_comprobante)

        # Información de contacto de la panaderia alineada a la izquierda
        c.setFont("Helvetica", 10)
        c.drawString(30, alto - 115, direccion_panaderia)
        c.drawString(30, alto - 130, correo_panaderia)
        c.drawString(30, alto - 145, telefono_panaderia)
        c.drawString(30, alto - 160, web_panaderia)

        # Detalles de la factura alineados a la derecha debajo del subtítulo
        c.setFont("Helvetica", 10)
        c.drawString(405, alto - 115, f'Fecha: {fecha_factura}')
        c.drawString(405, alto - 130, f'Tipo de venta: {tipo_venta}')
        c.drawString(405, alto - 145, f'Tipo de pago: {tipo_pago}')
        c.drawString(405, alto - 160, f'Núm. Comprobante: {nro_comprobante}')

        # Datos para la tabla
        data = [["DESCRIPCIÓN", "PRECIO UNITARIO", "CANT.", "IMPORTE"]]
        for item in items_de_venta:
            producto_nombre = item.producto.descripcion
            producto_precio = item.producto.precio
            cantidad = item.cantidad
            subtotal = item.subtotal
            data.append([producto_nombre,f'{producto_precio}',f'{cantidad}',f'{subtotal}'])

        # Crear la tabla con estilo
        table = Table(data, colWidths=[283, 100, 50, 100])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#3186BF')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BACKGROUND', (0, 1), (-1, -1), colors.whitesmoke),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ]))

        # Establecer posición de la tabla
        table.wrapOn(c, 30, alto - 250)
        table.drawOn(c, 30, alto - 250)


        #total debajo de la tabla
        y_pos_totals = alto - 300 - len(items_de_venta) * 20

        c.setFont("Helvetica-Bold", 10)
        c.drawString(490, y_pos_totals - 40, 'Total:')
        c.drawString(520, y_pos_totals - 40, f'{venta.total}')

        # Guardar y cerrar el archivo
        c.showPage()
        c.save()

    return response

def estadisticas(request):
    empleados = Empleado.objects.annotate(nro_ventas=Count('ventas_realizadas')).order_by('-nro_ventas')

    return render(request,'ventas/estadisticas.html',{'empleados':empleados})