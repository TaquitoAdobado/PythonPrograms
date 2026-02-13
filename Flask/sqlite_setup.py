# Para usar SQLite debemos importar el modulo sqlite3
import sqlite3

# Importamos Flask y g
from flask import Flask, g
    #g es un objeto global que se usa para almacenar datos durante el ciclo de vida de una solicitud.

# Creamos nuestra app de Flask como normalmente.
app = Flask(__name__)

# Creamos una constante para almacenar el nombre de la db con su ruta si no quieres que se cree en la raiz del proyecto.
DATABASE = "Flask/instance/midb.db"

# Creamos una funcion para abrir una conexion a la db y guardarla en g.
def get_db():

    # Verificamos que no exista una conexion previa.
    if "db" not in g:

        #abrimos nueva conexion.
        g.db = sqlite3.connect(DATABASE)

        #La siguiente linea hace que los resultados de las consultas se devuelvan como diccionarios en vez de tuplas.
        #row_factory guarda referencia a la clase Row de sqlite3.
        #Este paso es necesario para acceder a los datos de las filas por nombre de columna en lugar de por indices.
        g.db.row_factory = sqlite3.Row 
        """
        Sin row_factory
        cursor = db.execute("SELECT id, nombre FROM usuarios")
        row = cursor.fetchone()
        print(row[0])       # acceso por índice
        print(row[1])       # acceso por índice

        Con row_factory = sqlite3.Row
        cursor = db.execute("SELECT id, nombre FROM usuarios")
        row = cursor.fetchone()
        print(row["id"])    # acceso por nombre de columna
        print(row["nombre"])
        """

    # Devolvemos la conexion a la base de datos almacenada en g.
    return g.db

# Se debe crear una funcion para cerar la conexion a la db cuando se termina la solicitud.

# El decorador @app.teardown.appcontext indica que la funcion se ejecuta automaticamente al terminar el ciclo de vida de una solicitud.
# exception contiene la excepción (si ocurrió alguna) durante la request. Es obligatorio declararlo porque Flask lo envía

@app.teardown_appcontext
def close_db(exception):

    # Usamos g.pop para eliminar la conexion a la db que esta en g y lo almacenamos en una variable, si no existe devuelve None.
    db = g.pop("db", None)

    #Si db no es None, significa que si hay una conexion abierta.
    if db is not None:
        #Cerramos la conexion.
        db.close()

@app.route('/')
def index():
    # Obtenemos la conexion a la db
    db = get_db()

    # Ejecutamos una consulta SQL que devuelve un texto con el alias "mensaje".
    cursor = db.execute("SELECT 'Hola, SQLITE!' AS mensaje")

    # Obtenemos la primera fila del resultado de la consulta con .fetchone().
    # En este caso solo hay una fila con una columna llamada "mensaje".
    row = cursor.fetchone()

    # Accedemos al valor de la columna "mensaje" y la devolvemos como respuesta en la ruta principal.
    return row["mensaje"]

if __name__=="__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")