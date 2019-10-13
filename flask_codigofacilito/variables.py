from flask import Flask
from flask import render_template
from flask import request

# VARIABLES, CICLOS Y CONDICIONES + TEMPLATES

app = Flask(__name__)

@app.route('/user/')
@app.route('/user/<name>')
@app.route('/user/<name>/')
@app.route('/user/<name>/<int:edad>/')
def user(name='parametro vacio', edad = ''):
    my_list  = [1,3,4,5,66,4]
    return render_template('user.html', nombre_usuario = name, edad_usuario = edad, lista = my_list)

if __name__ == '__main__':
    app.run(debug=True, port=8000)