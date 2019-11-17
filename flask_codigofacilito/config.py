import os # Variables de entorno

class Config(object):
    SECRET_KEY  = 'my_secret_key'
    POSTS_PER_PAGE = 3

# Clase para definir las configuraciones del entorno de desarrollo
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123@localhost/flask'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
# Se prodría tener un entorno de pruebas

# Se prodría tener un entorno de producción

