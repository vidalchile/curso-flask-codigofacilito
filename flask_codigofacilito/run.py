# https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

from flask import Flask
from flask import render_template
from flask import request
from flask_wtf.csrf import CSRFProtect
from flask import make_response
from flask import session
from flask import redirect
from flask import url_for
from flask import flash
import forms
import json

# SERVICIO WEB
# RUTAS Y PARAMATROS
# VARIABLES, CICLOS Y CONDICIONES
# TEMPLATE
# HERENCIAS Y PLANTILLAS
# FORMULARIOS
# VALIDACIONES FORMULARIOS
# VALIDACIONES PROPIAS, CAMPOS HIDDEN
# CSRF Protection
# Cookies
# Session
# Flashed messages
# Control error 404
# AJAX
# Before request / after request

app = Flask(__name__)
app.secret_key = 'my_secret_key' # Identificador unico
csrf = CSRFProtect(app)

@app.before_request
def before_request():
    print('1')
    if 'username' not in session:        
        print(request.endpoint) # url peticion
        print('El usuario necesita login')

@app.after_request
def after_request(response):
    print('3')
    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error_404.html'), 404

@app.route('/')
def index():
    print('2')
    if 'username' in session:
        username = session['username']
        print('Valor Session: {}'.format(username))
    
    custom_cookie = request.cookies.get('custom_cookie')
    print('Valor Cookie: {}'.format(custom_cookie))
    return render_template('index.html')
 
@app.route('/usuario')
def usuario():
    nombre_usuario = 'Cristian'
    return render_template('user.html', nombre = nombre_usuario)

@app.route('/clientes')
def clientes():
    nombres = ['cliente 1', 'cliete 2', 'cliente 3', 'cliente 4']
    return render_template('client.html', nombres_clientes = nombres)

@app.route('/login', methods=['GET', 'POST'])
def login():
    formulario_login = forms.LoginForm(request.form)
    if request.method == 'POST' and formulario_login.validate():
        username = formulario_login.username.data
        session['username'] = username
        success_message = 'Bienvenido {}'.format(username)
        flash(success_message)
        print(username)
        print(formulario_login.password.data)

    titulo = 'Login'
    return render_template('login.html', title=titulo, form = formulario_login)

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    if 'username' in session:
        session.pop('username')
    return redirect(url_for('login'))

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    formulario = forms.CommentForm(request.form)
    
    if request.method == 'POST' and formulario.validate():
        print(formulario.username.data)
        print(formulario.email.data)
        print(formulario.comment.data)

    titulo = 'Formulario'
    return render_template('formulario.html', title=titulo, form = formulario)

@app.route('/cookie')
def cookie():
    response = make_response(render_template('cookie.html'))
    response.set_cookie('custom_cookie', 'Cristian Vidal')
    return response

@app.route('/ajax-login', methods=['POST'])
def ajax_login():
    # por ahora vamos a simular que el usuario se va a regirstrar
    username = request.form['username']
    response = {'status':200, 'username':username, 'id':'1'}
    return json.dumps(response), 200

if __name__ == '__main__':
    app.run(debug=True, port=8000)