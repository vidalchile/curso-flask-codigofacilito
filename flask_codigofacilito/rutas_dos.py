from flask import Flask
from flask import request

# RUTAS Y PARAMETROS

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hola mundo'

@app.route('/saluda')
def saluda():
    return 'Otro mensaje'

@app.route('/params/')
@app.route('/params/<name>')
@app.route('/params/<name>/<int:num>')
def params(name = '', num = 0):
    return 'El parametro es {}, {} '.format(name, num)

if __name__ == '__main__':
    app.run(debug=True, port=8000)