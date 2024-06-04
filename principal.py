from flask import Flask, send_file

app = Flask(__name__, static_folder='/')

@app.route("/")
def hello_world():
    return send_file('HTML/inicio.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
