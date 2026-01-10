#Para configurar un entorno Flask, sigue estos pasos:
#1. Instala Flask usando pip install flask
#2. Crea un archivo llamado app.py y agrega el siguiente código básico:

from flask import Flask     # Importa la clase Flask desde el módulo flask

app = Flask(__name__)       # Crea una instancia de la clase Flask
@app.route('/')             # Define una ruta para la URL raíz

def hello_world():
    '''Función que devuelve un saludo en HTML que se observa en el navegador'''

    return '<h1>Hello World!</h1>'

if __name__ == '__main__':  # Verifica si el script se está ejecutando directamente
    app.run(debug=True)     # Inicia la aplicación Flask en modo de depuración

#Si debug esta en False, no se recarga automáticamente al hacer cambios en el código.

#3. Ejecuta la aplicación, abre tu navegador y ve a http://localhost:5000 para ver tu aplicación en acción.
# Alternativa a localhost: Puedes usar la ip que se muestra al iniciar la app.
#¡Disfruta desarrollando con Flask!
