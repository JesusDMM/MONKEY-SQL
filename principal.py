from flask import Flask, render_template, request, jsonify
from analizadores.analizador_lexico import *
from analizadores.Analizador_Sintactico_Consultas import *
from analizadores.analizador_semantico import AnalizadorSemantico
from database.main import *

app = Flask(__name__, static_folder='static')

global base

def formatear_arbol(arbol, indent=0):
    espacio = ''
    resultado = []

    for elemento in arbol:
        if isinstance(elemento, list):
            resultado.append('\n' + espacio * indent + '[')
            resultado.append(formatear_arbol(elemento, indent + 1))
            resultado.append(espacio * indent + ']')
        elif isinstance(elemento, tuple):
            resultado.append(espacio * indent + str(elemento))
        else:
            resultado.append(espacio * indent + repr(elemento))

    return '\n'.join(resultado)


@app.route("/")
def principal():
    conexion_bd = conexion('escuela')
    estructura = obtener_estructura_bd(conexion_bd)
    global base
    base = estructura
    print(base)
    return render_template('index.html')

@app.route('/semantico')
def semantico():
    return render_template('semantico.html') 

@app.route('/api/v1/analizador_lexico', methods=['POST'])
def analizador_lexico():
    data = request.get_json()
    consulta = data['texto']
    
    if consulta is None or consulta.strip() == "":
        return jsonify({"Errore": 'Consulta vacía'}), 400
    
    tokens, errores, tok = tokenizar(consulta)
    
    errores_formateados = ''
    if len(errores) > 0:
        errores_formateados = '\n'.join(
            [', '.join(errores[i:i+4]) for i in range(0, len(errores), 4)]
        )
        return jsonify({'Error': errores_formateados}), 200
    
    tokens_formateados = '\n'.join(
        [', '.join(map(str, tokens[i:i+4])) for i in range(0, len(tokens), 4)]
    )
    
    arbol, errores_sintacticos = analizar_consulta(consulta)
    print(arbol)
    
    if len(errores_sintacticos) > 0:
        return jsonify({'Error': errores_formateados,
                        'Error_sintactico': errores_sintacticos}), 200

    arbol_formateado = formatear_arbol(arbol)
    
    global base
    
    analizador_semantico = AnalizadorSemantico(base)
    
    analizador_semantico.analizar(arbol)
    
    errores_semanticos = analizador_semantico.obtener_errores()
    
    if len(errores_semanticos) > 0:
        return jsonify({'Error': errores_formateados,
                        'Error_sintactico': errores_sintacticos,
                        'Error_semantico': errores_semanticos}), 200

    return jsonify({'Tokens': tokens_formateados,
                    'Error': errores_formateados,
                    'Arbol_sintactico': arbol_formateado,
                    'Error_sintactico': errores_sintacticos,
                    'Semantico': 'Sin errores semanticos',
                    'Error_semantico': errores_semanticos}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
