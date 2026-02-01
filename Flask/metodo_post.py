# POST Se usa para enviar datos al servidor (crear, modificar, procesar información).
# Los parámetros se envían en el cuerpo de la petición, no en la URL.
# No es idempotente: cada envío puede producir un cambio (ej. guardar en base de datos).

from flask import Flask, render_template, request
app = Flask(__name__)

#Creamos una ruta para renderizar un formualario.
#El navegador enviara los datos del formulario al servidor en el cuerpo de una solicitud POST.
@app.route('/')
def formulario_post():
    return render_template('formulario_post.html')

#El servidor recibe la solicitud del navegador, captura y procesa los datos en la ruta definida.
#Se debe especificar el metodo HTTP, en este caso POST.
@app.route('/post' , methods=['POST'])
def metodo_post():

    #A diferencia de GET, usamos request.form.get('dato a capturar').
    user: str = request.form.get('user')
    password: str = request.form.get('password')
    
    #Se procesa la informacion devolviendo al navegador un mensaje con los datos capturados.
    return f"""
    <h1>Usuario ingresado: {user}</h1>
    <h1>Contraseña ingresada: {password}</h1>
    <h1>Has usado el metodo POST. Los datos no son visibles en la URL.</h1>
    """

if __name__=='__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')