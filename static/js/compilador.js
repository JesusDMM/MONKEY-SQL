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
                throw new Error('Ingrese una consulta primero');
            }
            return response.json();
        })
        .then(data => {
            if (data.Error) {
                error_lexico = 'Error lexico: ' + data.Error
                document.getElementById('sql-output').value = error_lexico;
                return;
            }
            if (data.Error_sintactico) {
                error_sintactico = 'Error sintactico: ' + data.Error_sintactico
                document.getElementById('sql-output').value = error_sintactico;
                return;
            }
            if (data.Error_semantico) {
                error_semantico = 'Error semantico: ' + data.Error_semantico
                document.getElementById('sql-output').value = error_semantico;
                return;
            }
            if (data.Error_execucion) {
                error_execucion = 'Error de execucion: ' + data.Error_execucion
                document.getElementById('sql-output').value = error_execucion;
                return;
            }
            salida = 'Tokens del analizador lexico: ' + '\n'
                + data.Tokens + '\n'
                + 'Arbol sintactico: ' + '\n'
                + data.Arbol_sintactico + '\n'
                + 'Respuesta del analizador semantico:' + '\n'
                + data.Semantico

            document.getElementById('sql-output').value = salida;

            const jsonData = JSON.parse(data.Informacion);

            actualizarTabla(jsonData)

        })
        .catch(error => {
            document.getElementById('sql-output').value = 'Error: ' + error.message;
        });
});

function actualizarTabla(jsonData) {
    if (!jsonData || jsonData.length === 0) {
        console.error('jsonData está vacío o no está definido.');
        return;
    }

    console.log(jsonData);

    const tableContainer = document.querySelector('.table-container');
    if (!tableContainer) {
        console.error('No se encontró la clase .table-container.');
        return;
    }

    const table = tableContainer.querySelector('table');
    if (!table) {
        console.error('No se encontró la tabla.');
        return;
    }

    const tbody = table.querySelector('tbody');
    const thead = table.querySelector('thead');
    const headerRow = thead.querySelector('tr');

    headerRow.innerHTML = '';
    tbody.innerHTML = '';

    const firstRow = jsonData[0];
    const properties = Object.keys(firstRow);

    properties.forEach(property => {
        const th = document.createElement('th');
        th.textContent = property;
        headerRow.appendChild(th);
    });

    for (const dataRow of jsonData) {
        const row = document.createElement('tr');
        console.log(dataRow);

        for (const key in dataRow) {
            const cell = document.createElement('td');
            cell.textContent = dataRow[key];
            row.appendChild(cell);
        }

        tbody.appendChild(row);
    }
}