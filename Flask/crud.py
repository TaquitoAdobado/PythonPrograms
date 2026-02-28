# CRUD describe las 4 operaciones basicas que se realizan sobre datos en una base de datos:
# Crear(Create), Leer(Read), Actualizar(UPDATE) y Borrar(Delete)
# En este archivo se realizara la logica para cada una de las operaciones CRUD
"""
archivos usados:
    templates/crud/
        - base.html
        - nav_bar.html
        - new_user.html
        - read_users.html
        - form_user_email.html
        - form_update_user.html
    
    static/
        - style.css
        - script.js
    
    instance/
        - crud.db (Se crea al iniciar la app, seria mejor crearlo antes y por separado en un init_db.py)
"""

import sqlite3
from flask import Flask, render_template, request, g

app = Flask(__name__,template_folder="templates/crud/")
DATABASE = "Flask/instance/crud.db"

# -------------------- Conexion DB --------------------
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

# -------------------- CREATE (tabla usuarios) --------------------
def create_table_users():
    """ CREATE -> Crea la tabla usuarios si no existe """

    #Primero obtenemos la conexion a la base de datos.
    db = get_db()

    # Luego usamos .execute el cual es un metodo que ejecuta una sola sentencia SQL.
    db.execute("""CREATE TABLE IF NOT EXISTS usuarios (
               id INTEGER PRIMARY KEY,
               nombre TEXT NOT NULL,
               apellido TEXT NOT NULL,
               email TEXT NOT NULL UNIQUE,
               password TEXT NOT NULL);""")
    
    # Finalizamos con .commit() el cual es un metodo que guarda los cambios realizados.
    db.commit()

    # El ciclo de vida de la solicitud termina y se cierra automaticamente la conexion a la db gracias a la funcion close_db().


# -------------------- CREATE (crear usuario) --------------------

@app.route('/usuario_creado', methods = ['POST'])
def post_create_user():

    db = get_db()

    # Capturamos los datos del formulario para crear un usuario 
    u_nombre: str = request.form.get("nombre_usuario").capitalize()
    u_apellido: str = request.form.get("apellido_usuario").capitalize()
    u_email : str = request.form.get("email_usuario")
    u_password: str = request.form.get("password_usuario")
    
    # Sentencia SQL para agregar los datos del usuario en la DB, si hay conflico de email no hace nada.
    cursor = db.execute("""INSERT INTO usuarios (nombre, apellido, email, password) VALUES(
               ?, ?, ?, ?) ON CONFLICT (email) DO NOTHING""",(u_nombre, u_apellido, u_email, u_password))
    db.commit()

    # Se revisa si se registró un cambio en la DB, si no hubo cambio es porque hubo conflicto con el email (ya existia).
    if cursor.rowcount == 0:
        return f"""
    <h2>Fallo al registrar usuario. El email {u_email} ya se encuentra registrado. </h2>
    <p>Regresar a la pagina de <a href="/inicio">Inicio</a></p>
    """
    else:
        return f"""
    <h2>Usuario {u_nombre} {u_apellido} registrado exitosamente.</h2>
    <p>Regresar a la pagina de <a href="/inicio">Inicio</a></p>
    """

# -------------------- READ (usuarios)--------------------
def read_users():

    db = get_db()
    # Ejecutamos la sentencia SQL para el READ del CRUD
    cursor = db.execute("SELECT id, nombre, apellido, email FROM usuarios")
    # Retornamos toda la respuesta para usarla en la ruta "/leer/usuarios".
    return cursor.fetchall()


# -------------------- UPDATE --------------------
@app.route('/actualizando/usuario', methods = ['POST'])
def update_user():
    db=get_db()

    # Se revisa que valor se captura para decidir si buscar al usuario o actualizarlo con los datos capturados.
    if not request.form.get("nombre_usuario"):

        # *** Captura de email y devolucion de datos del usuario para actualizar ***
        correo = request.form.get("email_usuario")
        cursor = db.execute("""SELECT nombre, apellido, email FROM usuarios WHERE email = ?""",(correo,))
        datos_usuario = cursor.fetchone()
        # Si la sentencia SQL no devuelve nada, usuario no registrado.
        if not datos_usuario:
            return f"""
            <h2>El email {correo} no se encuentra registrado.</h2>
            <p>Regresar a la pagina de <a href="/inicio">Inicio</a></p>"""
        else:
            return render_template("form_update_user.html", usuario=datos_usuario)
        
    else:
        # *** Captura de datos y actualizacion de usuario ***
        correo_actual = request.form.get("email_actual")
        nuevo_nombre = request.form.get("nombre_usuario").capitalize()
        nuevo_apellido = request.form.get("apellido_usuario").capitalize()
        nuevo_email = request.form.get("email_usuario")
        db.execute(""" UPDATE usuarios SET
                   nombre = ?,
                   apellido = ?,
                   email = ?
                   WHERE email = ?""", (nuevo_nombre, nuevo_apellido, nuevo_email, correo_actual))
        db.commit()
        return f"""
        <h1>Usuario actualizado exitosamente.</h1>
        <p>Regresar a la pagina de <a href="/inicio">Inicio</a></p>"""
# -------------------- DELETE --------------------





# -------------------------------------------------------------------------------------

# -------------------- RUTAS --------------------
@app.route('/inicio')
def page_home():
    return render_template("base.html")


@app.route('/crear/usuario')
def page_form_create_user():
    return render_template('new_user.html')
    

@app.route('/leer/usuarios')
def page_read_users():
    usuarios = read_users()
    return render_template('read_users.html', usuarios=usuarios)


@app.route('/actualizar/usuario')
def page_update_user():
    return render_template("form_user_email.html")

# -------------------- MAIN --------------------
if __name__ == "__main__":
    #usando with app.app_context(): se asegura de que la base de datos se cree antes de iniciar el servidor
    with app.app_context():
        create_table_users()
    
    app.run(debug=True, port=5000, host="0.0.0.0")