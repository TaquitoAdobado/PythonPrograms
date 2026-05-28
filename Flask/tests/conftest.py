'''
Archivos usados:
    Flask/
        prueba_test.py
        tests/
            conftest.py
            test_home.py
'''
# Que es conftest.
# Este archivo "conftest.py" es un archivo especial que reconoce pytest sin necesidad de ser importado cada vez.
# En este archivo se definen fixures globales (recursos de prueba compartidos) que se usaran en todos los tests.

# Que hace conftest.
# Centraliza configuraciones de prueba (evita repetir codigo en cada test).
# Proporciona fixtures -> funciones que preparan un entorno de prueba (ej. Cliente de Flask, db temporales, usuario de prueba.)

# Instalaciones:
# Primero instalemos la libreria "pytest" (Para testing) con: pip install pytest
# Adicionalmente instalaremos pytest-html (Para reportes mas detallados) con: pip install pytest-html

# Importemos pytest
import pytest

# Ahora importemos la instancia de flask de nuestra app principal (usaremos de ejemplo prueba_test.py)
from prueba_test import app

# Creamos un fixture usando pytest.fixture como decorador. Recordemos que fixture es una funcion.
@pytest.fixture
def client():
    '''
    Fixture que crea un cliente de flask

    - test_client es un método de Flask que crea un cliente de pruebas HTTP.
        Permite simular llamadas a tus rutas (GET, POST, etc.) sin levantar el servidor real.

    - El with abre un contexto controlado:
        Inicializa el cliente.
        Se asegura de cerrarlo correctamente al terminar la prueba.
    '''
    # Configuramos el entorno de testing
    app.config["TESTING"] = True

    # Creamos un cliente de prueba flask
    with app.test_client() as client:
        # Entregamos el cliente a los tests
        yield client

# Ahora creemos los tests en archivos dentro de la carpeta "tests", el nombre del archivo debe empezar con "test_".

# Creemos el test "test_home.py para probar la ruta principal "/home" de nuestra app prueba_test.py