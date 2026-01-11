#Para configurar un entorno Flask, sigue estos pasos:

#Instala Flask usando pip install flask
#Crea un archivo llamado app.py y agrega el siguiente código básico:

from flask import Flask     # Importa la clase Flask desde el módulo flask

app = Flask(__name__)       # Crea una instancia de la clase Flask, __name_ es el nombre del módulo actual

@app.route('/')             # Define una ruta para la URL raíz, 127.0.0.1:5000/ o http://localhost:5000/
def hello_world():
    '''Función que devuelve un saludo en HTML que se observa en el navegador'''

    return '<h1>Hello World!</h1>'  # Devuelve un mensaje HTML cuando se accede a la ruta raíz

if __name__ == '__main__':  # Verifica si el script se está ejecutando directamente
    app.run(debug=True, port=5000, host = '0.0.0.0')     # Inicia la aplicación Flask

# debug=True activa el modo de depuración, lo que proporciona mensajes de error detallados y recarga automática.
#port=5000 especifica el puerto en el que se ejecutará la aplicación (5000 es el valor predeterminado).
#host= '0.0.0.0' permite que la aplicación sea accesible desde cualquier dispositivo local usando la IP de la maquina.

#Ejecuta la aplicación, abre tu navegador y ve a http://localhost:5000 o http://127.0.0.1:5000 para ver tu aplicación en acción.
#Accede desde tu telefono usando la IP local de tu computadora seguida del puerto 5000 (ejemplo: http://192.168.0.185:5000)
#¡Disfruta desarrollando con Flask!

#Nota: Este archivo generalmente se llama app.py o main.py