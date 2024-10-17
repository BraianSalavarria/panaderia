function convertirFecha(fechaStr) {
    // Crear un diccionario para mapear los meses en español a números
    const meses = {
        "enero": "01",
        "febrero": "02",
        "marzo": "03",
        "abril": "04",
        "mayo": "05",
        "junio": "06",
        "julio": "07",
        "agosto": "08",
        "septiembre": "09",
        "octubre": "10",
        "noviembre": "11",
        "diciembre": "12"
    };

    // Dividir la cadena para obtener día, mes y año
    let [dia, mesTexto, año] = fechaStr.toLowerCase().split(" ");

    // Convertir el mes de texto a número usando el diccionario
    let mes = meses[mesTexto];

    // Devolver la fecha en el formato deseado: YYYY/MM/DD
    return `${año}-${mes}-${dia.padStart(2, '0')}`;
}





// Función para abrir el modal y asignar los valores de la categoría

    function modalEditarCategoria(id, nombre) {
        // Asignar los valores al modal

        document.getElementById('categoriaId').value = id;
        document.getElementById('categoriaNombre').value = nombre;

        // Mostrar el modal
        var modal = new bootstrap.Modal(document.getElementById('modalEditarCategoria'));
        modal.show();
    }


    function modalEliminarCategoria(categoriaId) {
        // Configura la URL del botón de confirmación en el modal
        const urlEliminar = `eliminar-categoria/${categoriaId}`
        document.getElementById('confirmarEliminar').setAttribute('href', urlEliminar);

        // Muestra el modal de eliminación
        const modal = new bootstrap.Modal(document.getElementById('modalEliminar'));
        modal.show();
    }


    function filtrarTablaCategorias(){
    document.getElementById("buscarProducto").addEventListener("input", function() {
        const filter = this.value.toLowerCase();
        const rows = document.querySelectorAll("#tablaContenido tbody tr");
    
        rows.forEach(row => {
            const descripcion = row.cells[1].textContent.toLowerCase();
            if (descripcion.includes(filter)) {
                row.style.display = "";
            } else {
                row.style.display = "none";
            }
        });
    });
}

function modalEditarProducto(id_producto,descripcion,cantidad,id_categoria,precio) {
        // Asignar los valores al modal
            document.getElementById('id_producto').value = id_producto;
            document.getElementById('descripcionProductoM').value = descripcion;
            document.getElementById('precioProductoM').value = precio;
            document.getElementById('cantidadProductoM').value = cantidad;
            document.getElementById('categoriaProductoM').value = id_categoria;

        // Mostrar el modal
        var modal = new bootstrap.Modal(document.getElementById('modalEditarProducto'));
        modal.show();
    }


    function filtrarTablaProductos(){
        document.getElementById("buscarProducto").addEventListener("input", function() {
            const filter = this.value.toLowerCase();
            const rows = document.querySelectorAll("#tablaContenido tbody tr");
        
            rows.forEach(row => {
                const descripcion = row.cells[1].textContent.toLowerCase();
                if (descripcion.includes(filter)) {
                    row.style.display = "";
                } else {
                    row.style.display = "none";
                }
            });
        });
    }


    function modalEliminarProducto(productoId) {
        // Configura la URL del botón de confirmación en el modal
        const urlEliminar = `eliminar-producto/${productoId}`
        document.getElementById('confirmarEliminar').setAttribute('href', urlEliminar);

        // Muestra el modal de eliminación
        const modal = new bootstrap.Modal(document.getElementById('modalEliminar'));
        modal.show();
    }

    function modalEditarMayorista(id,cuil,nombre,apellido,info) {
        // Asignar los valores al modal
            document.getElementById('id_mayorista').value = id;
            document.getElementById('cuilMayoristaM').value = cuil;
            document.getElementById('nombreMayoristaM').value = nombre;
            document.getElementById('apellidoMayoristaM').value = apellido;
            document.getElementById('informacionMayoristaM').innerText = info;

        // Mostrar el modal
        var modal = new bootstrap.Modal(document.getElementById('modalEditarMayorista'));
        modal.show();
    }

    function modalInfoMayorista(info){

         // Asignar los valores al modal
        document.getElementById('infoMayoristaM').innerText = info;
         // Mostrar el modal
        var modal = new bootstrap.Modal(document.getElementById('modalInfoMayorista'));
        modal.show();
    }

    function modalEliminarMayorista(id_mayorista){

         // Configura la URL del botón de confirmación en el modal
        const urlEliminar = `eliminar-mayorista/${id_mayorista}`
        document.getElementById('confirmarEliminar').setAttribute('href', urlEliminar);

        // Muestra el modal de eliminación
        const modal = new bootstrap.Modal(document.getElementById('modalEliminar'));
        modal.show();

    }

    function modalEditarEmpleado(id_empleado,nombre,apellido,cuil,fechaNacimiento,celular,fijo,calle,nroCalle,localidad,departamento,fechaIngreso) {

            fechaNac = convertirFecha(fechaNacimiento)
        // Asignar los valores al modal
            document.getElementById('id_empleado').value = id_empleado;
            document.getElementById('nombreEmpleado').value = nombre;
            document.getElementById('apellidoEmpleado').value = apellido;
            document.getElementById('cuitEmpleado').value = cuil;
            fechaNac = convertirFecha(fechaNacimiento)
            document.getElementById('fechaNacimiento').value = fechaNac;
            document.getElementById('telefonoCelularEmpleado').value = celular;
            document.getElementById('telefonoFijoEmpleado').value = fijo;
            document.getElementById('calle').value = calle;
            document.getElementById('numeroCalle').value = nroCalle;
            document.getElementById('localidad').value = localidad;
            document.getElementById('departamento').value = departamento;
            
            fechaIng = convertirFecha(fechaIngreso)
            document.getElementById('fechaIngreso').value = fechaIng;
            
        // Mostrar el modal
         var modal = new bootstrap.Modal(document.getElementById('modalEditarEmpleado'));
        modal.show();

    }

     function modalEliminarEmpleado(id_empleado){

         // Configura la URL del botón de confirmación en el modal
        const urlEliminar = `eliminar-empleado/${id_empleado}`
        document.getElementById('confirmarEliminar').setAttribute('href', urlEliminar);

        // Muestra el modal de eliminación
        const modal = new bootstrap.Modal(document.getElementById('modalEliminar'));
        modal.show();
    }

    function modalInfoEmpleado(nombre,apellido,cuil,fechaNacimiento,celular,fijo,calle,nroCalle,localidad,departamento,fechaIngreso) {

            fechaIng = convertirFecha(fechaIngreso)
            fechaNac = convertirFecha(fechaNacimiento)
        // Asignar los valores al modal

            document.getElementById('nombreEmpleadoI').value = nombre;
            document.getElementById('apellidoEmpleadoI').value = apellido;
            document.getElementById('cuitEmpleadoI').value = cuil;
            document.getElementById('fechaNacimientoI').value = fechaNac;
            document.getElementById('telefonoCelularEmpleadoI').value = celular;
            document.getElementById('telefonoFijoEmpleadoI').value = fijo;
            document.getElementById('calleI').value = calle;
            document.getElementById('numeroCalleI').value = nroCalle;
            document.getElementById('localidadI').value = localidad;
            document.getElementById('departamentoI').value = departamento;
            document.getElementById('fechaIngresoI').value = fechaIng;

            const modal = new bootstrap.Modal(document.getElementById('modalInfoEmpleado'));
            modal.show();
    }
