# En este archivo se prueba la ruta home usando el fixture client de conftest.

def test_home_route(client):
    # Simulamos una solicitud GET a la ruta "/home"
    response = client.get("/home")

    # Ahora usamos assert para verificar una serie de condiciones que definiran si la prueba paso o no
    # Si un assert falla, la prueba falla y se devuelve un error llamado AssertionError
    assert response.status_code == 200
    # La b es para indicar que estamos trabajando con bytes, ya que la respuesta del servidor es en bytes
    assert b"Hello World" in response.data


# Hemos terminado. Para correr la prueba, se hace desde la terminal, estando parados sobre la carpeta raiz de la app
# y usamos el comando: pytest -v
# Se nos mostraran los resultados generales de las pruebas, si pasan o si hay errores.
# -v nos detalla los resultados de las pruebas mencionando la ruta y el estado de la prueba


# Tambien podemos estar sobre la carpeta que contiene la app (si no es la carpeta raiz) y usar el comando:
# python -m pytest -v


# Recordemos que instalamos pytest-html para un reporte mas detallado, para generar el reporte html usamos:
# pytest -v --html=report.html
# o dado el caso de la carpeta que contiene la app:
# python -m pytest -v --html=report.html


# El archivo report.html se genera en la carpeta raiz de la app y podemos abrirlo con cualquier navegador