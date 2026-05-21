# En este archivo usaremos los entornos definidos en config.py
# Importamos Flask como usualmente y aparte importamos el entorno de configuracion que usaremos

from flask import Flask
from config import DevConfig, TestConfig

# Creamos nuestra app
app = Flask(__name__)

# Ahora seleccionemos el entorno de configuracion usando "app.config.from_object()".
app.config.from_object(DevConfig)

# Ahora podemos usar las variables de entorno en nuestra app sin tener que declararlas.

# Por ejemplo nuestra SECRET_KEY
print(app.config['SECRET_KEY']) # Salida: clave_segura

# Ahora revisemos la ruta de nuestra base de datos
print(app.config['DATABASE_PATH']) # /instance/midatabase.db

# Ahora usemos el entorno de testing, en el que la ruta de la base de datos cambia
app.config.from_object(TestConfig)

print(app.config['DATABASE_PATH']) # /instance/test.db