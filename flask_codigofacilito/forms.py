from wtforms import Form, BooleanField, StringField, TextField, PasswordField, validators
from wtforms.fields.html5 import EmailField

# Este archivo prodría tener todos los formularios

class CommentForm(Form):
    username = StringField('username')
    email = EmailField('Correo electronico')
    comment = TextField('Comentario')