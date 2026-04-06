# Flash es un contenedor de mensajes que se muestran en la parte superior de la pagina.
# Para usar flash debemos importar el modulo flash de flask
from flask import Flask, render_template,flash
from pathlib import Path

app = Flask(
    __name__,
    template_folder= Path(__file__).parent / "templates"
    )

# Flash() guarda los mensajes en la sesion del usuario y Flask los protege con una firma digital "secret_key".
# Si no se define, flask no garantiza la seguridad y puede bloquear la sesion.

''' Para definir la secret_key, se puede usar un str aleatorio: app.secret_key = "mi_secret_key" 
    Es mala practica exponerla en el codigo. '''

''' Otra opcion es usar una variable de entorno y llamarla con os.environ.get("NOMBRE_VARIABLE", "valor_por_defecto")

        Para esto necesitamos importar el modulo os y crear la variable de entorno desde la terminal de la siguiente manera:
            ```Windows powershell
            $env:SECRET_KEY="mi_clave_de_entorno_super_secreta_y_segura"
            python app.py    # Ejecutamos la app desde la terminal posicionados en la carpeta de la app
            ```

            ```Linux bash/macOS
            export SECRET_KEY="mi_clave_de_entorno_super_secreta_y_segura"
            python app.py    # Ejecutamos la app desde la terminal posicionados en la carpeta de la app
            ```
'''
import os

# Llamamos una variable de entorno para la secret key
app.secret_key = os.environ.get("SECRET_KEY", "clave_default")
print(f"clave usada: {app.secret_key}") #Puse esto para observar la clave usada solamente.


'''
    La ultima forma de definir la secret key es usando un archivo .env.

    Para esto debemos instalar el modulo python-dotenv usando pip install:
        pip install python-dotenv

    Luego creamos el archivo .env en la carpeta de la app:
    proyecto/
        app.py
        .env
    
    Este archivo .env tendra las variables de entorno:
        SECRET_KEY=clave_segura
        FLASK_APP= app.py
        FLASK_ENV=development

    En app.py debemos importar el modulo dotenv:
        from dotenv import load_dotenv

    Luego cargamos el archivo .env con la funcion:
        load_dotenv()
        
    Por ultimo ya podemos declarar la secret key con la variable de entorno:
        app.secret_key = os.environ.get("SECRET_KEY", "clave_default")
        
    CONSIDERACIONES:
    - Los archivos .env no deben ser publicos por lo que deben estar en la carpeta .gitignore.
    '''


@app.route("/inicio")
def inicio():
    # En flash() se usan 2 parametros: el mensaje y el tipo de mensaje, en este caso "info" (podria ser cualquier palabra).
    flash("Bienvenido a la pagina de inicio", "info")
    # Luego tenemos que configurar el bloque messages en el html a mostrar el mensaje.
    # Revisar archivo flash_messages.html

    # Renderizamos la plantilla para ver el mensaje
    return render_template("flash_message.html")


app.run(debug=True, port=5000, host='0.0.0.0')