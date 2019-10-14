from flask import Flask
from flask import render_template
from flask import request

# HERENCIAS Y PLANTILLAS

app = Flask(__name__)

@app.route('/')
def index():
    nombre_usuario = 'Cristian'
    return render_template('index.html', nombre = nombre_usuario)

@app.route('/client')
def client():
    nombres = ['cliente 1', 'cliete 2', 'cliente 3', 'cliente 4']
    return render_template('client.html', nombres_clientes = nombres)

if __name__ == '__main__':
    app.run(debug=True, port=8000)