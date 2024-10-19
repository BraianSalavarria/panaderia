from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from Apps.empleados.forms import EmpleadoForm
from Apps.inventario.forms import ProveedorForm
from Apps.inventario.models import Proveedor


def lista_proveedores(request):
    proveedores = Proveedor.objects.all()
    proveedor_form = ProveedorForm()
    return render(request, 'inventario/administrarProveedores.html',{'form':proveedor_form ,'proveedores':proveedores})

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

def editar_proveedor(request):
    if request.method == 'POST':
        proveedor = get_object_or_404(Proveedor, id = request.POST['id_proveedor'])
        proveedor.nombre = request.POST['nombreProveedorM']
        proveedor.apellido = request.POST['apellidoProveedorM']
        proveedor.empresa = request.POST['empresaM']

        proveedor.save()
        messages.success(request,f'Proveedor "{proveedor.nombre}" Actualizado Correctamente')
        return redirect(to='inventario:lista_proveedores')



def eliminar_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, id=id)
    proveedor.delete()
    messages.success(request,f'Proveedor "{proveedor.nombre}" Eliminado Exitosamente')
    return  redirect(to='inventario:lista_proveedores')