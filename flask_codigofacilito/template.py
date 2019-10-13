from flask import Flask
from flask import render_template
from flask import request

# TEMPLATES

# app = Flask(__name__, template_folder='prueba_template')
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=8000)