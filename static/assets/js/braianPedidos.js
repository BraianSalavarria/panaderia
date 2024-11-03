document.addEventListener('DOMContentLoaded', () =>{
    generarNroComprobante();
})

function generarNroComprobante(){
 var min = 000000000000;
     var max = 999999999999;
     var x = Math.floor(Math.random()*(max-min+1)+min);
     document.getElementById('nro_pedido').value = x;
}
