


function filtrarTabla(){
    const filtro = document.getElementById('filtro').value.toLowerCase();
    let filas =  document.querySelectorAll('#tablaFiltro tbody tr');

    filas.forEach(function(fila){
        const textoFila = fila.textContent.toLowerCase();
        fila.style.display = textoFila.includes(filtro) ? '':'none';
    });
}

document.getElementById('filtro').addEventListener('input', filtrarTabla);