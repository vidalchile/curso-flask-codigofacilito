import os # Variables de entorno

class Config(object):
    SECRET_KEY  = 'my_secret_key'

# Clase para definir las configuraciones del entorno de desarrollo
class DevelopmentConfig(Config):
    DEBUG = True

# Se prodría tener un entorno de pruebas

# Se prodría tener un entorno de producción

