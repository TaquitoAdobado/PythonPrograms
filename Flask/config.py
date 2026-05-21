# El archivo config.py contiene el entorno de configuración que se usara en app.py (el archivo principal de la app)
# Podemos tener diferentes configuraciones para distintos entornos: dev, test, prod
# Estos entornos tendrán las variables de entorno que usaremos en la app.py
# Tambien incluiremos el path a nuestra base de datos (declarado en .env) o su URI si usamos SQLAlchemy
""" Archivos usados:
    - app.py
    .env (recordemos incluirlo en el gitignore y nunca exponerlo)
"""

# Primero carguemos las variables de entorno
from dotenv import load_dotenv
import os
load_dotenv()


# Los presets los definimos usando Clases. Para ello primero definamos una clase con todas las variables de entorno

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    DATABASE_PATH = os.getenv("DATABASE_URL")

# Ahora definamos los diferentes entornos que podriamos usar

# Para el entorno de desarrollo
class DevConfig(Config):
    DEBUG = True
    TESTING = False

# Para el entorno de testing
class TestConfig(Config):
    DEBUG = True
    TESTING = True
    DATABASE_PATH = "instance/test.db"

# Para el entorno de produccion
class ProdConfig(Config):
    DEBUG = False
    TESTING = False


# Ahora usaremos estas configuraciones en nuestra aplicacion principal. En este caso app.py
    


