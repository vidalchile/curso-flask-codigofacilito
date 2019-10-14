from flask import Flask
from flask import render_template
from flask import request

# SERVICIO WEB
# RUTAS Y PARAMATROS
# VARIABLES, CICLOS Y CONDICIONES
# TEMPLATE
# HERENCIAS Y PLANTILLAS

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
 
@app.route('/usuario')
def usuario():
    nombre_usuario = 'Cristian'
    return render_template('user.html', nombre = nombre_usuario)

@app.route('/clientes')
def clientes():
    nombres = ['cliente 1', 'cliete 2', 'cliente 3', 'cliente 4']
    return render_template('client.html', nombres_clientes = nombres)

@app.route('/contacto')
def contacto():
    return 'pendiente pagina de contacto'

if __name__ == '__main__':
    app.run(debug=True, port=8000)