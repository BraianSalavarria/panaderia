from multiprocessing.util import close_all_fds_except
from optparse import check_builtin

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from Apps.empleados.forms import EmpleadoForm
from Apps.empleados.models import Empleado


# Create your views here.

def lista_empleados(request):
    empleados = Empleado.objects.all()
    empleado_form = EmpleadoForm()
    return render(request,'empleados/administrarEmpleados.html',{'form':empleado_form,'empleados':empleados})


def agregar_empleado(request):
    empleados = Empleado.objects.all()

    if request.method == 'POST':
        empleado_form = EmpleadoForm(request.POST)
        if empleado_form.is_valid():
            empleado_form.save()
            messages.success(request,f'Empleado "{empleado_form.cleaned_data['nombre']}" Registrado con Exito')
            return redirect(to='empleados:lista_empleados')
        else:
            # Si el formulario no es válido, renderiza la página con los errores
            return render(request, 'empleados/administrarEmpleados.html', {
                'empleados': empleados,
                'form': empleado_form,
                'errors': empleado_form.errors
            })

def editar_empleado(request):

    if request.method == 'POST':
        empleado_actualizado = get_object_or_404(Empleado,id=request.POST['id_empleado'])

        nombre = request.POST['nombreEmpleado']
        apellido = request.POST['apellidoEmpleado']
        cuil = request.POST['cuitEmpleado']
        fechaNac = request.POST['fechaNacimiento']
        fecha_ingreso = request.POST['fechaIngreso']
        celular = request.POST['telefonoCelularEmpleado']
        fijo = request.POST['telefonoCelularEmpleado']
        calle = request.POST['calle']
        nro_calle = request.POST['numeroCalle']
        localidad = request.POST['localidad']
        dpto = request.POST['departamento']

        empleado_actualizado.nombre = nombre
        empleado_actualizado.apellido = apellido
        empleado_actualizado.cuil = cuil
        empleado_actualizado.fecha_nacimiento = fechaNac
        empleado_actualizado.telefono_celular = celular
        empleado_actualizado.telefono_fijo = fijo
        empleado_actualizado.fecha_ingreso = fecha_ingreso
        empleado_actualizado.calle = calle
        empleado_actualizado.nro_calle = nro_calle
        empleado_actualizado.localidad = localidad
        empleado_actualizado.dpto = dpto

        empleado_actualizado.save()
        messages.success(request, f'Empleado "{nombre}" Actualizado Correctamente')

    return redirect(to='empleados:lista_empleados')


def eliminar_empleado(request,id):

   empleado_eliminado = get_object_or_404(Empleado,id = id)
   empleado_eliminado.delete()
   messages.success(request,f'Empleado "{empleado_eliminado.nombre}" Eliminado Exitosamente')
   return redirect(to='empleados:lista_empleados')



