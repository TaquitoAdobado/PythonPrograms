#Para renderizar una plantilla(template) en Flask, se utiliza la función render_template del módulo flask.
#Esta funcion se importa desde la libreria flask.

from flask import Flask, render_template

#Creamos la instancia de la aplicacion Flask como normalmente se hace.
app = Flask(__name__)

#Definimos una ruta para la aplicacion.
@app.route('/')

#Al definir la ruta, creamos una funcion que se ejecutara cuando se acceda a esa ruta.
def template_example():
    #Esta funcion usa el metodo render_template para importar y renderizar el contenido de una plantilla HTML.

    return render_template('index.html') #index.html es el nombre del archivo de la plantilla que queremos importar.
    #Esta plantilla contiene el contenido HTML que se mostrara en el navegador cuando se acceda a la ruta '/'.

#Finalmente, ejecutamos la aplicacion Flask.
if __name__ == '__main__':
    app.run(debug=True, port = 5000, host = '0.0.0.0')


'''
Flask por defecto sabe que los templates se encuentran en la carpeta templates/
Si por algun motivo cambiamos el nombre de esa carpeta, para que flask pueda encontrarlos debemos agregarlo al crear la instancia.
Ejemplo, la carpeta templates se renombra a plantillas:
app = Flask(__name__, template_folder="plantillas")
'''