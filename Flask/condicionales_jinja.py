# Condicionales en Jinja2 con Flask
from flask import Flask, render_template, request
app = Flask(__name__)

#Definimos una ruta para mostrar la condicional if con un parametro dinamico en la URL.
@app.route('/if/condicional/<int:edad>')
def condicional_if(edad):
    '''
    Verifica si la edad proporcionada en la URL es mayor o menor de edad.
    
    Args:
        edad: numero entero colocado en la URL (int).
    
    Returns:
        str: plantilla HTML renderizada con el resultado de la verificacion.
        
    Example:
        URL: http://127.0.0.1:5000/if/condicional/18
        Resultado: "Es mayor de edad."
    '''

    #Renderizmos la plantilla html con el parametro edad.
    return render_template("condicionales_jinja.html", edad=edad)


#Definimos una ruta para mostrar el condicional for con un parametro dinamico en la URL.
@app.route('/for/condicional/<int:numero>')
def condicional_for(numero):
    '''
    Devuelve una lista de numeros hasta el numero dado en la URL
    
    Args:
        numero: numero entero colocado en la URL (int).
    
    Returns:
        str: Plantilla HTML renderizada con un listado de numeros hasta el dado en la url.
    
    Example:
        URL: http://127.0.0.1:5000/for/condicional/10
        Resultado:
            1
            2
            ...
            9
            10
    
    Nota: No usar valores demasiado grandes para evitar errores de memoria, en este ejemplo no hay manejo de errores.
    '''

    return render_template("condicionales_jinja.html", numero=numero)

if __name__=="__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')