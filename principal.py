from flask import Flask, render_template

app = Flask(__name__, static_folder='static')

@app.route("/")
def principal():
    return render_template('index.html')

@app.route('/semantico')
def semantico():
    return render_template('semantico.html') 

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
