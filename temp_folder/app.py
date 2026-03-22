from flask import Flask
from extensions import db
from models import User
from pathlib import Path


# 1. Se crea la instancia de Flask
app = Flask(
    __name__,
    instance_path= Path(__file__).parent / 'instance')

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
