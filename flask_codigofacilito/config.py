import os # Variables de entorno

class Config(object):
    SECRET_KEY  = 'my_secret_key'
    POSTS_PER_PAGE = 3
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT =  587
    MAIL_USE_SSL = False
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'cvm@autopress.cl'
    MAIL_PASSWORD = os.environ.get('PASSWORD_EMAIL')

# Clase para definir las configuraciones del entorno de desarrollo
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123@localhost/flask'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
# Se prodría tener un entorno de pruebas

# Se prodría tener un entorno de producción

