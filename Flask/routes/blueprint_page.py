# Las blueprints son una manera de agrupar rutas y templates en un archivo separado que se puede importar en el archivo principal de la app.

# Para usar blueprints debemos importar el modulo Blueprint de flask
from flask import Blueprint

# Creamos una instancia de Blueprint que representa la ruta que importaremos al archivo principal de la app.
pagina_bp = Blueprint('blueprint_page', __name__) # Como parametros usamos: nombre del archivo, __name__

# Creamos la funcion que se ejecutara cuando se acceda a esa ruta y usamos de decorador el nombre de la instancia de Blueprint y su ruta.
@pagina_bp.route('/paginabp')
def blueprint_page():
    return "<h1>Esta es la pagina de blueprint</h1>"

# Ahora pasamos a la app principal blueprint.py