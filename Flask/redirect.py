#La funcion redirect() se utiliza para redirigir a los usuarios a una URL diferente.
#Es util para casos como al iniciar sesion, despues de enviar un formulario, etc.

from flask import Flask, redirect, url_for

app = Flask(__name__)


#Ruta teorica de inicio de sesion exitoso, redirige al usuario a la pagina principal.
@app.route('/login')
def login():
    
    # Redireccionamos a la ruta definida en la funcion pagina_inicio por medio de url_for()
    return redirect(url_for('pagina_inicio'))


@app.route('/inicio')
def pagina_inicio():
    return "<h1>Bienvenido a la pagina de inicio</h1>"

if __name__=="__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")


#Corre el codigo y accede a /login para ver la redireccion a /inicio