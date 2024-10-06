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
                error_lexico = 'Error lexico: ' + data.Error
                document.getElementById('sql-output').value = error_lexico;
                return;
            }
            if (data.Error_sintactico.length > 0) {
                error_sintactico = 'Error sintactico: ' + data.Error_sintactico
                document.getElementById('sql-output').value = error_sintactico;
                return;
            }
            if (data.Error_semantico.length > 0) {
                error_semantico = 'Error semantico: ' + data.Error_semantico
                document.getElementById('sql-output').value = error_semantico;
                return;
            }
            salida = 'Tokens del analizador lexico: ' + '\n'
                + data.Tokens + '\n'
                + 'Arbol sintactico: ' + '\n'
                + data.Arbol_sintactico + '\n'
                + 'Respuesta del analizador semantico:' + '\n'
                + data.Semantico
            document.getElementById('sql-output').value = salida;
        })
        .catch(error => {
            document.getElementById('sql-output').value = 'Error: ' + error.message;
        });
});
