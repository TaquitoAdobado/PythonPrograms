"""NOTA: Este archivo no es para probar usando RUN Python File, es para explicar como usar session
    Sientete libre de tomarlo y adaptarlo como referencia para tu proyecto personal o de estudio. """


# Session en Flask es un diccionario de variables de sesión que se almacena en una coockie en el navegador del usuario.
# Sirve para mantener información temporal sobre el usuario mientras navega por la aplicación.
# Una sesión se inicia cuando el usuario inicia sesión y se finaliza cuando el usuario cierra sesión.


""" session aplica una firma digital "secret_key" a las cockies para garantizar la seguridad, esta firma se debe declarar como una 
variable de entorno o tenerla en el archivo .env
NUNCA debe exponerse ya que puede ser usada para ataques.
Para este caso vamos a:
- instalar el modulo python-dotenv usando pip install
- crear el archivo .env en la carpeta de la app y luego vamos a declarar la secret key de la siguiente manera:
    SECRET_KEY = clave_segura
    (recuerda agregar .env a tu gitignore para no exponer la secret key)
- En nuestra app.py importamos la funcion load_dotenv de la libreria dotenv.
- Tmambien importaremos la libreria os
- Luego cargaremos el archivo .env en nuestra app.py usando la funcion importada:
    load_dotenv()
- Por ultimo delcaramos una variable con la secret key de la siguiente manera:
    app.secret_key = os.environ.get("SECRET_KEY")"""

from flask import Flask, request, session
from dotenv import load_dotenv
import os


app = Flask(__name__)
load_dotenv()
app.secret_key = os.environ.get("SECRET_KEY")   #Con esto ya tenemos preparado todo para usar session.

#Despues de realizar las validaciones de usuario y contraseña podemos usar session para almacenar la informacion del usuario.
"""
*El usuario envia sus datos de login a traves de un formulario.

username = request.form.get('username')
email = request.form.get('email')
password = request.form.get('password')

*Validaciones de usuario y contraseña correctas

# Almacenar la informacion del usuario en la sesion
session['username'] = username
session['email'] = email
"""

#Con la informacion del usuario almacenada, tenemos una sesion activa y podemos hacer por ejemplo una pagina de perfil.

"""
@app.route('/perfil')
def profile_page():
    #si existe una sesion activa muestra la pagina de perfil
    if "username" in session:
        return f"<h1>Bienvenido {session['username']}</h1>"
    
    #si no existe una sesion activa redirige al login
    else:
        return redirect(url_for('login'))
"""

#Para cerrar la sesion y limpiar la informacion de la sesion usamos la funcion session.clear()

"""
# Ruta para cerrar la sesion
@app.route('/logout')
def logout():
    session.clear()                     #Limpia la informacion de la sesion
    return redirect(url_for('inicio'))  #Redirige al inicio
"""