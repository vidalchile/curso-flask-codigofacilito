from flask import Flask

# HOLA MUNDO

app = Flask(__name__) # Nuevo objeto

@app.route('/') # utilizamos un decorador, el indica al servidor ruta disponibles
def index(): # funcion retorna un string
    return 'Hola mundo'

app.run() # iniciar nuestro servidor por default en puerto 5000

