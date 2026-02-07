#Flask permite capturar errores HTTP y personalizar la respuesta que se envia al cliente.
from flask import Flask, render_template

#En este ejemplo capturamos el error 404 y renderizamos un template personalizado como respuesta.

app = Flask(__name__)

@app.route('/')
def inicio():
    return "<h1>Bienvenido a la página de inicio</h1>"


#El error 404 indica Pagina no encontrada, o sea, no existe.
@app.errorhandler(404)
def pagina_no_encontrada(error):
    #El 404 despues del render indica el codigo de estado HTTP que se enviara al navegador.
    #Flask lo interpreta como una tupla: (respuesta, codigo_estado)
    return render_template("404.html"), 404

#Intenta cambiar la url para obsrevar el error 404.

if __name__=="__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")


""" Los diferentes errores a capturar con HTTP mas comunes son:

400 - Bad request: Indica que el cliente envió una petición mal formada (por ejemplo datos faltantes o incorrectos)

401 - Unauthorized: El usuario no esta autenticado (No ha iniciado sesion).

403 - Forbidden: El usuario esta autenticado pero no tiene permisos.

404 - Not Found: La URL solicitada no existe.

405 - Method Not Allowed: El método HTTP usado no está permitido para esa ruta.
(Usar POST en una ruta solo GET, Usar GET en una ruta DELETE)

408 - Request Timeout: El cliente tardó demasiado en enviar la petición. (Conexiones lentas, problemas de red, requests muy pesados).

409 - Conflict: Hay un conflicto de datos. (Usuario duplicado, registro ya existe)

500 - Internal Server Error: Error interno del servidor. (Bug en el código, excepción no controlada, fallo de base de datos)


"""