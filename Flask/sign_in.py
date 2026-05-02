# En este script se muestra como realizar un registro de usuario con werkzeug.security mediante un formulario HTML.
""" Archivos utilizados:
sign_in.html
signin_home.html
...
"""
# Importamos las librerias necesarias

from flask import Flask, render_template, request, g
from werkzeug.security import generate_password_hash
import sqlite3

# Creamos nuestra app y definimos la base de datos
app = Flask(__name__)
DATABASE = "Flask/instance/sign_in.db"

# Preparamos una funcion para la conexion y la desconexion a la base de datos
def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db

@app.teardown_appcontext
def close_db(exception):
    db = g.pop("db", None)
    if db is not None:
        db.close
    
def create_table_users():
    db= get_db()
    db.execute("""CREATE TABLE IF NOT EXISTS usuarios (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               username TEXT NOT NULL,
               password TEXT NOT NULL,
               email TEXT NOT NULL UNIQUE);""")
    
def read_users():
    db = get_db()
    # Ejecutamos la sentencia SQL para el READ del CRUD
    cursor = db.execute("SELECT id, username, email, password FROM usuarios")
    # Retornamos toda la respuesta para usarla en la ruta "/leer/usuarios".
    return cursor.fetchall()

# Ruta de registro. Si no se ha enviado formulario, se muestra el formulario. Si ya se ha enviado formulario, se muestra un mensaje de exito
@app.route('/registro', methods=['GET', 'POST'])
def signin_page():
    if request.method == 'GET':
        return render_template('sign_in.html')
    
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
        <p>Regresar a la pagina de <a href="/inicio">Inicio</a></p>"""

    return f"""
    <h1>El email {email} ya está en uso por otro usuario.</h1>
    <p>Regresar a la pagina de <a href="/inicio">Inicio</a></p>"""
    


@app.route('/inicio')
def home_page():
    return render_template("signin_home.html")

@app.route('/leer')
def page_read_users():
    usuarios = read_users()
    return f""" <h1>Usuarios registrados:</h1>
    <ul>
        {"".join(f"<li>{usuario['username']} - {usuario['email']}</li>" for usuario in usuarios)}
    </ul>
    <p>Regresar a la pagina de <a href="/inicio">Inicio</a></p>"""
    

if __name__ == '__main__':
    with app.app_context():
        create_table_users()
    app.run(debug=True, port=5000, host='0.0.0.0')