
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