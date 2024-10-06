document.getElementById('boton_consulta').addEventListener('click', function () {
    const consulta = document.getElementById('sql-input').value;

    const datos = {
        texto: consulta
    };

    fetch('/api/v1/analizador_lexico', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(datos)
    })
        .then(response => {
            if (!response.ok) {
                throw new Error('Error en la solicitud: ' + response.status);
            }
            return response.json();
        })
        .then(data => {
            if (data.Error.length > 0) {
                document.getElementById('sql-output').value = data.Error;
            } else {
                document.getElementById('sql-output').value = data.Tokens;
            }
        })
        .catch(error => {
            document.getElementById('sql-output').value = 'Error: ' + error.message;
        });
});
