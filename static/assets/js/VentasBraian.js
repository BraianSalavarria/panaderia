/*
let categoriaSelect = document.getElementById('categoriaSelect');
  let productoSelect = document.getElementById('productoSelect');
  let cantidad = document.getElementById('cantidad');

  let totalFacturado = document.getElementById('id_total');
  let venta = 0;
  let tablaProductos = document.getElementById('tablaProductos').getElementsByTagName('tbody')[0];

  function cargarTabla(){
    producto_id = productoSelect.value;
    let cant = parseInt(cantidad.value);
  
     
      if(producto_id && cant >0 ) {
      
          fetch(`obtener-producto/${producto_id}`)
          
          .then(response => response.json())

          .then(data => {

            if(data.producto) {
              let producto = data.producto;
              let total = (parseFloat(producto.precio)* cant).toFixed(2);
              venta = (parseFloat(venta) + parseFloat(total)).toFixed(2);
              console.log(venta)
              totalFacturado.value = venta;



              // agregamos el elemeto a la tablaProductos

              let nuevaFila = tablaProductos.insertRow();
              nuevaFila.innerHTML = `
                <td>${producto.id}</td>
                <td>${producto.descripcion}</td>
                <td>${cant}</td>
                <td>${producto.precio}</td>
                <td>${total}</td>
                <td><button type="button" class="btn btn-danger btn-sm" onclick="eliminarFila(this,${total})">Eliminar</button></td>
              
              `;
            } else {
                alert('producto no encontrado')
                }
            
          })
            .catch(erro => console.error('error al obtener el produco', error));
      }
  }

  function eliminarFila(btn, total ){
    // Eliminar la fila de la tabla
    let fila = btn.parentNode.parentNode;
    totalVenta = totalVenta - total;
    

    fila.parentNode.removeChild(fila);
}

*/
