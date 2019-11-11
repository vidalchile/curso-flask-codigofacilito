from wtforms import Form, BooleanField, StringField, TextField, PasswordField, validators
from wtforms.fields.html5 import EmailField
from wtforms import HiddenField
from models import User

# Validaciones propias
def length_honeypot(form, field):
    if len(field.data) > 0:
        raise validators.ValidationError('Error campo debe estar vacío.')

class LoginForm(Form):
    
    username = StringField('username',
    [
        validators.Required(),
        validators.Length(min=4, max=25, message='Ingrese un username valido!')
    ])
    
    password = PasswordField('Contraseña', [
        validators.Required()
    ])

class CreateUserForm(Form):
    
    username = StringField('username',
    [
        validators.Required(),
        validators.Length(min=4, max=25, message='Ingrese un username valido!')
    ])
    
    password = PasswordField('Contraseña', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords no coincide')
    ])

    confirm = PasswordField('Repetir contraseña')

    email = EmailField('Correo electronico',
    [
        validators.Required(),
        validators.Email(message='Ingrese un email valido!')
    ])

    # Sobreescribiendo metodo
    def validate_username(form, field):
        username = field.data
        user = User.query.filter_by(username = username).first()
        if user is not None:
            raise validators.ValidationError('El username {} ya se encuentra registrado!'.format(username))

class CommentForm(Form):
    comment = TextField('Comentario')
    honeypot = HiddenField('', [length_honeypot])