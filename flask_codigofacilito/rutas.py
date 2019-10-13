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

@app.route('/params')
def params():
    param = request.args.get('params1', 'no contiene este parametro')
    params2 = request.args.get('params2', 'no contiene este parametro')
    return 'El parametro es {}, {} '.format(param, params2)

if __name__ == '__main__':
    app.run(debug=True, port=8000)