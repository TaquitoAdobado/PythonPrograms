# En este archivo se explica como importar blueprints en Flask.
''' Archivos usados:
    routes/blueprint_page.py'''

# Importamos nuestra blueprint

from routes.blueprint_page import pagina_bp
from flask import Flask

# Creamos nuestra instancia de Flask como normalmente
app = Flask(__name__)

# Ahora registramos nuestra blueprint
app.register_blueprint(pagina_bp) 
# Podemos agregar un prefijo en la url si usamos como 2do parametro:
    # url_prefix="/prefix"

# Corremos nuestro servidor y probamos que se pueda acceder a la ruta (http://127.0.0.1:5000/paginabp)
app.run(debug=True, port=5000, host='0.0.0.0')