from flask import Flask, jsonify, render_template, request
from extensions import db
from models import User
from pathlib import Path
from sqlalchemy.exc import IntegrityError

# 1. Se crea la instancia de Flask
app = Flask(
    __name__,
    instance_path= Path(__file__).parent / 'instance',
    template_folder= Path(__file__).parent / 'templates')

# Ruta absoluta hacia la base de datos dentro de "instance"
db_path = app.instance_path / 'database.db'

# 2. Configuramos la conexión a la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_path}"

''' 
URI = Uniform Resource Identifier
Cadena de texto estandarizada para identificar un recurso, en SQLAlchemy se usan los siguientes elementos: 
    - Dialecto -> Motor de base de datos (sqlite, mysql, postgresql,etc)
    - Driver -> Conector de la base de datos (pymysql, psycopg2, etc). / SQLite no necesita un driver
    - usuario:contrasena -> Credenciales de acceso. / SQLite no necesita credenciales
    - host:puerto -> Direccion del servidor y puerto. / SQlite no necesita host y puerto
    - database -> Nombre de la db. / SQLite usa la ruta absoluta de la db (con nombre de la db y extension .db)
'''

# 3. Desactivamos el rastreo de modificaciones
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

'''
Si esta en True, SQLAlchemy rastrea los cambios en los objetos y dispara señales.
Genera overhead (consumo extra de memoria/CPU) porque mantiene registros de los cambios.
'''

# 4. Vinculamos la extensión SQLAlchemy con la app
db.init_app(app)
'''
db.init_app(app) es el paso que conecta tu objeto db con tu aplicación Flask. 
Sin esto, tus modelos no sabrían a qué base de datos conectarse ni qué configuración usar
'''

# 5. Creamos la base de datos con sus tablas definidas en models
with app.app_context():
    db.create_all()
'''
- app_context es como un “entorno” que le dice a Flask: usa esta instancia de app para todo lo que hagas ahora.
- Sin ese contexto, db.create_all() no sabe a qué aplicación ni a qué base de datos conectarse.
'''

# 6. Creamos las rutas

# -------------------- READ --------------------
def get_users():
    users = User.query.all() # SELECT * FROM users
    return users


# -------------------- CREATE --------------------
@app.route('/usuario_creado', methods=['POST'])
def create_user():
    first_name = request.form.get("user_first_name").capitalize()
    last_name = request.form.get("user_last_name").capitalize()
    age = request.form.get("user_age")
    email = request.form.get("user_email")

    user = User(first_name=first_name, last_name=last_name, age=age, email=email)
    db.session.add(user) # Se marca el objeto a insertar
    return commit_rollback(user, f"Usuario {user.first_name} {user.last_name} creado exitosamente.")


# -------------------- FILTER FOR UPDATE OR DELETE --------------------
@app.route('/buscando/usuario', methods=['POST'])
def find_user():
    user_email = request.form.get("email_usuario")
    action = request.form.get("action") # action = actualizar o eliminar
    user = User.query.filter_by(email=user_email).first() # SELECT * FROM users WHERE email = ?

    if not user:
        return f"""<h2>El email {user_email} no se encuentra registrado.</h2>
        <p>Regresar a la pagina de <a href="/inicio">Inicio</a></p>"""
    
    if action == "actualizar":
        return render_template("form_update_user.html", user=user)

    elif action == "eliminar":
        pass
        # return render_template("form_delete_user.html", user=user)


# -------------------- UPDATE --------------------
@app.route('/usuario/actualizado', methods=['POST'])
def update_user():
    user_email = request.form.get("email_actual")
    new_first_name = request.form.get("nombre_usuario").capitalize()
    new_last_name = request.form.get("apellido_usuario").capitalize()
    new_age = request.form.get("edad_usuario")
    new_email = request.form.get("email_usuario")

    user = User.query.filter_by(email=user_email).first()
    user.first_name = new_first_name
    user.last_name = new_last_name
    user.age = new_age
    user.email = new_email

    return commit_rollback(user, f"Usuario {user.first_name} {user.last_name} actualizado exitosamente.")


#-------------------- Funcion auxiliar --------------------
def commit_rollback(user,success_message):
    ''' 
    Funcion auxiliar que realiza commit y rollback en caso de error. Por ahora solo maneja IntegrityError
    por email duplicado.
    Parametros:
        user: Objeto User
        success_message: Mensaje de confirmacion
    '''
    try:
        db.session.commit() # Se ejecuta sentencia SQL
        return f"""<p>{success_message}</p>
        <p>Regresar a <a href="/inicio">Inicio</a></p>"""
    
    except IntegrityError: # Si hay un error de integridad (email duplicado). El email esta marcado como UNIQUE
        db.session.rollback()
        return f"""<p>Error: El email {user.email} ya se encuentra registrado.</p>
        <p>Regresar a <a href="/inicio">Inicio</a></p>"""


# -------------------- PAGINAS --------------------
@app.route('/inicio')
def home_page():
    return render_template("base.html")
                           

@app.route('/crear/usuario')
def add_user_page():
    return render_template("new_user.html")

@app.route('/leer/usuarios')
def read_users_page():
    users_data = get_users()
    return render_template("read_users.html", users=users_data)

@app.route('/actualizar/usuario')
def update_user_page():
    return render_template("form_user_email.html", action="actualizar", title="Update (crUd)")

# 7. Ejecutamos la app
if __name__ == '__main__':
    app.run(debug=True, port = 5000, host = '0.0.0.0')