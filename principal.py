from flask import Flask, render_template, request, jsonify
from analizadores.analizador_lexico import *

app = Flask(__name__, static_folder='static')

@app.route("/")
def principal():
    return render_template('index.html')

@app.route('/semantico')
def semantico():
    return render_template('semantico.html') 

@app.route('/api/v1/analizador_lexico', methods=['POST'])
def crear_usuario():
    data = request.get_json()
    consulta = data['texto']
    if consulta is None or consulta.strip() == "":
        return jsonify({"Errore": 'Consulta vacía'}), 400
    tokens, errores, tok = tokenizar(consulta)
    
    tokens_formateados = '\n'.join(
        [', '.join(map(str, tokens[i:i+4])) for i in range(0, len(tokens), 4)]
    )
    
    errores_formateados = '\n'.join(
        [', '.join(errores[i:i+4]) for i in range(0, len(errores), 4)]
    )
    
    return jsonify({'Tokens': tokens_formateados,
                    'Error': errores_formateados}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
