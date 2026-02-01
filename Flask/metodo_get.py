#GET: Se usa principalmente para solicitar datos al servidor.
#Envia una solicitud al servidor con datos reflejados en la URL y el servidor responde con los datos solicitados.
#Es idempotente: pedir lo mismo varias veces no debería cambiar nada en el servidor.

#Para poder usar estos metodos, se debe importar request desde flask.
from flask import Flask, render_template, request
app = Flask(__name__)


#Establecemos una ruta para renderizar un formulario.
#Con el formulario, el navegador construye un URL con los datos y los envia al servidor.
@app.route('/')
def formulario():
    return render_template('formulario_get.html')

#El servidor recibe la solicitud del navegador, captura y procesa los datos en la ruta definida.
#Se debe especificar el metodo HTTP, en este caso GET.
@app.route('/get', methods=['GET'])
def metodo_get():
    #Para capturar ese dato, se usa request.args.get('dato a capturar')
    usuario = request.args.get('usuario')
    #Se procesa la informacion devolviendo al navegador un mensaje con el dato capturado.
    return f'<h1> Hola, {usuario}, has usado el metodo GET.</h1>'

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')