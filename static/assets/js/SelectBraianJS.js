document.addEventListener('DOMContentLoaded', () =>{
    generarNroComprobante();
})

function generarNroComprobante(){
 var min = 000000000000;
     var max = 999999999999;
     var x = Math.floor(Math.random()*(max-min+1)+min);
     document.getElementById('id_nro_comprobante').value = x;
}

  $(document).ready(function () {
    // Esta línea asegura que el código dentro de la función se ejecute
    // solo después de que todo el contenido HTML de la página se haya cargado por completo.

    $("#categoriaSelect").change(function () {
        // Escucha el evento 'change' en el elemento con id 'categoriaSelect'.
        // Es decir, cuando el usuario selecciona una categoría diferente, se activa esta función.

        const categoriaId = $(this).val();
        console.log(categoriaId)
        // Obtiene el valor seleccionado del elemento 'categoriaSelect' (por ejemplo, el id de la categoría).

        if (categoriaId) {
            // Verifica si 'categoriaId' tiene algún valor (es decir, si se seleccionó alguna categoría).

            $.ajax({
                url: 'obtener-productos', // Especifica la URL del servidor donde se enviará la solicitud.
                type: "GET", // Define el tipo de solicitud HTTP (GET en este caso).
                data: { categoria: categoriaId },
                // Envía los datos al servidor. Aquí, está enviando el 'categoriaId' como parámetro.

                success: function (data) {
                  console.log("si funciona")
                    // Esta función se ejecuta si la solicitud AJAX es exitosa.
                    // El parámetro 'data' contiene la respuesta del servidor.

                    $("#productoSelect").empty();
                    // Limpia el contenido actual del elemento 'productoSelect'.

                    $("#productoSelect").append('<option value="">Selecciona un producto</option>');
                    // Agrega una opción predeterminada en 'productoSelect' para que el usuario sepa que debe seleccionar un producto.

                    data.productos.forEach(function (producto) {
                        // Itera sobre cada producto recibido en la respuesta 'data'.

                        $("#productoSelect").append(
                            `<option value="${producto.id}">${producto.nombre}</option>`
                            // Agrega una nueva opción en el 'productoSelect' por cada producto.
                            // El 'value' será el 'id' del producto, y el texto visible será el 'nombre' del producto.
                        );
                    });
                },
                error: function (xhr, status, error) {
                  console.log('no pasa nada')
                    // Esta función se ejecuta si ocurre un error durante la solicitud AJAX.
                    console.error("Error al cargar los productos:", error);
                    // Muestra un mensaje de error en la consola para ayudar en la depuración.
                }
            });
        } else {
            // Si no hay ninguna categoría seleccionada (por ejemplo, si el usuario elige una opción vacía),
            // entonces se limpia el 'productoSelect'.
            $("#productoSelect").empty();
            $("#productoSelect").append('<option value="">Selecciona un producto</option>');
        }
    });
});



