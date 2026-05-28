# Archivo de prueba para pruebas unitarias de Flask con pytest.
from flask import Flask

app = Flask(__name__)

@app.route('/home')
def home(): 
    return "Hello World"

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')