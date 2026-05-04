"""ESTE ARCHIVO CONCLUYE EL CAPITULO 6 DE FLASK, EN ESTE TEMA "RESTRICCIONES DE RUTAS" SE USARA LO VISTO EN
hash_passwords.py, sing_up.py, y session.py

Archivos usados:
    - login.html
    - inicio.html
    - sign_up.html
    """

# Es muy comun que ciertas paginas tengan contenido restringido a las personas que no cumplan cierto requisito, por ejemplo, un login.
# Esto se puede realizar gracias al uso de decoradores y session.

#Antes que nada importemos las librerias necesarios, usaremos las librerias de flask, werkzeug.security, sqlite3, os y dotenv

from flask import Flask, render_template, request, g, session, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
import os
from dotenv import load_dotenv
import sqlite3

# Preparemos el servidor y las rutas de inicio y registro, despues de eso preparemos un login y al final veremos la restriccion de rutas.

# ----------------------------------------------------------Preparacion del servidor----------------------------------------------------------
# Cargamos las variables de entorno
load_dotenv() #Recordemos tener un archivo .env en la carpeta de la app con la secret key. (Revisar session.py para mas informacion)
# Creamos nuestra app
app = Flask(__name__)
# Definimos la secret key
app.secret_key = os.environ.get("SECRET_KEY")
# Definimos la base de datos
DATABASE = "Flask/instance/database_usuarios.db"


# Preparemos la conexion y la desconexion a la base de datos
def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db

@app.teardown_appcontext
def close_db(exception):
    db = g.pop("db", None)
    if db is not None:
        db.close()

#Preparemos la funcion para crear la tabla de usuarios
def create_table_users():
    db= get_db()
    db.execute("""CREATE TABLE IF NOT EXISTS usuarios (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               username TEXT NOT NULL,
               password TEXT NOT NULL,
               email TEXT NOT NULL UNIQUE);""")
    db.commit()

#Preparemos la funcion del singup para crear el usuario
@app.route('/registro', methods=['GET', 'POST'])
def signup_page():
    if request.method == 'GET':
        return render_template('sign_up.html')
    
    username = request.form.get('username')
    email = request.form.get('email')
    password = generate_password_hash(request.form.get('password'))

    db = get_db()
    # Comprobacion de email duplicado
    its_duplicated = db.execute("SELECT * FROM usuarios WHERE email = ?", (email,)).fetchone()
    if not its_duplicated:
        db.execute("INSERT INTO usuarios (username, password, email) VALUES (?,?,?)", (username, password, email))
        db.commit()
        return f"""<h1>Usuario {username} registrado exitosamente.</h1>
        <p>Regresar a la pagina de <a href="{url_for('home_page')}">Inicio</a></p>"""

    return f"""
    <h1>El email {email} ya está en uso por otro usuario.</h1>
    <p>Regresar a la pagina de <a href="{url_for('home_page')}">Inicio</a></p>"""
    
# Preparamos la pagina de inicio
@app.route('/inicio')
def home_page():
    return render_template("inicio.html")

# ----------------------------------------------------------------------------------------------------------------------------------------------------
# Hasta este punto solo hemos reciclado lo necesario del codigo de sign_up.py, ahora creemos una pagina de login

# Preparamos la pagina de login
@app.route('/login', methods=['GET', 'POST'])
def login_page():

    # Si el metodo es GET, se muestra el formulario
    if request.method == 'GET':
        return render_template('login.html')
    
    # Si el metodo es POST significa que el usuario esta logueandose, asi que comprobemos sus datos y capturemos los datos en session
    username = request.form.get('username')
    email = request.form.get('email')
    
    db = get_db()
    #Llamamos a la informacion del email ingresado en el formulario
    user = db.execute("SELECT * FROM usuarios WHERE email = ?", (email,)).fetchone()

    # Si no tenemos informacion, el email no esta registrado
    if not user:
        return f"""<h1>El email {email} no esta registrado.</h1>
        <p>Regresar a la pagina de <a href="{url_for('home_page')}">Inicio</a></p>"""
    
    # Si el email si existe, comprobamos la password de forma segura gracias a werkzeug
    validation = check_password_hash(user['password'], request.form.get('password'))
    if not validation:
        return f"""<h1>La contraseña es incorrecta.</h1>
        <p>Presione <a href="{url_for('login_page')}">aqui</a> para volver a intentarlo.</p>"""
    
    #Usemos lo que aprendimos en session.py
    #Si la password es correcta, creamos la sesion con la informacion del usuario y redirigimos al usuario a la pagina de inicio
    session["username"] = user['username']
    session["email"] = user['email']
    return redirect(url_for("home_page"))


# ----------------------------------------------------------------------------------------------------------------------------------------------------

# Ahora ya contamos con informacion almacenada en session, entonces creemos una pagina de perfil
# Pero que solo se pueda acceder a ella si el usuario esta logueado.
# Si el usuario no esta agregado, se le redirigira al login
# Para saber si un usuario esta logueado, podremos verificar que session tenga activo algun valor como "username" (visto en session.py).

#Preparemos un decorador para verificar si el usuario esta logueado.
def login_required(function):
    def wrap_login_required(*args, **kwargs):
        # Si no existe una sesion activa redirige al login
        if "username" not in session:
            return redirect(url_for("login_page"))
        # Si existe una sesion activa ejecuta la funcion a la que se decora
        return function(*args, **kwargs)           
    return wrap_login_required

# Preparemos la pagina de perfil y la decoramos con login_required

@app.route('/perfil')
@login_required
def profile_page():
    return f"""
    <h1>Bienvenido a tu perfil</h1>
    <p>Usuario: {session['username']}</p>
    <p>Email: {session['email']}</p>
    <p>Regresar a la pagina de <a href="{url_for('home_page')}">Inicio</a></p>
    """

# Preparemos el logout
@app.route('/logout')
def logout():
    if "username" in session:
        session.clear()
        return f"""
        <h1>Has cerrado la sesion exitosamente.</h1>
        <p>Regresar a la pagina de <a href="{url_for('home_page')}">Inicio</a></p>"""
    # Si no existe una sesion activa redirige a la pagina de inicio
    return redirect(url_for("home_page"))

if __name__ == '__main__':
    with app.app_context():
        create_table_users()
    app.run(debug=True, port=5000, host='0.0.0.0')