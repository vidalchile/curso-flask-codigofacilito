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
from flask import g
from  config import DevelopmentConfig
from models import db
from models import User
import forms
import json
from werkzeug.security import generate_password_hash

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
# Variables globales
# Configuraciones
# Coneccion base de datos, creacion de modelos, ORM SQLAlchemy
# Ingresar registros en la base de datos
# Form method override (Ejemplo: validar nombre de usuario único)

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect()

@app.before_request
def before_request():
    
    g.mi_variable_global = 'variable global 1'

    if 'username' not in session:        
        print(request.endpoint) # url peticion
        print('El usuario necesita login')

@app.after_request
def after_request(response):
    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error_404.html'), 404

@app.route('/')
def index():
    
    print(g.mi_variable_global)

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
    
    if form_is_valid(request.method, formulario_login):
        
        username = formulario_login.username.data
        password = formulario_login.password.data
        user = User.query.filter_by(username = username).first()

        if user is not None and user.verify_password(password):
            success_message = 'Bienvenido {}'.format(username)
            flash(success_message)
            session['username'] = username
            return redirect( url_for('index') )
        
        error_message = 'Usuario o contraseña incorrectas'
        flash(error_message)

    titulo = 'Iniciar sesion'
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

@app.route('/create-user', methods=['GET', 'POST'])
def crear_usuario():
    
    create_form = forms.CreateUserForm(request.form)
    
    if form_is_valid(request.method, create_form):
        username = create_form.username.data
        password = generate_password_hash(create_form.password.data)
        email = create_form.email.data
        user = User(username = username, password = password, email = email)
        db.session.add(user)
        db.session.commit()
        success_message = 'Usuario registrado en la base de datos'
        flash(success_message)

    titulo = 'Crear Usuario'
    return render_template('create_user.html', title=titulo, form = create_form)

def form_is_valid(method, form):
    if method == 'POST' and form.validate():
        return True
    return False

if __name__ == '__main__':

    csrf.init_app(app)
    
    db.init_app(app) # Obtiene todas las conf. de la DB
    with app.app_context():
        db.create_all() # si existe la tabla no las creara
    
    app.run(port=8000)