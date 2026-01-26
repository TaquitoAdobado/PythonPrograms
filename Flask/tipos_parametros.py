"""
Flask tiene distintos tipos de parámetros dinámicos, los cuales son:

- string : texto (es el valor por defecto)
- int    : números enteros
- float  : números decimales
- path   : texto que puede incluir '/'
- uuid   : identificadores únicos en formato estándar

Este archivo contiene ejemplos básicos de cada tipo de parámetro dinámico
para entender cómo Flask valida y convierte automáticamente los valores de la URL.
"""

from flask import Flask

app = Flask(__name__)

# Ruta con parametro string (valor por defecto)
@app.route('/string/<string:nombre>')
def parametro_string(nombre):
    '''
    Saluda al usuario usando un parámetro de tipo string. 
    Args:
        nombre: Nombre del usuario (string).
    
    Returns:
        str: mensaje de saludo

    Example:
        URL: /string/Daniel
    
    Resultado:
        Hola, Daniel, este es un parametro string.
    '''
    return f'<h1>Hola, {nombre}, este es un parametro string.</h1>'


#Ruta con parametro int
@app.route('/int/<int:id>')
def parametro_int(id):
    '''
    Muestra el ID del URL usando parametro int. 
    Args:
        id: ID numerico (int).
    
    Returns:
        str: mensaje con el ID

    Example:
        URL: /int/123456
    
    Resultado:
        El ID del URL es 123456 y es del tipo int.
    '''
    return f'<h1>El ID del URL es {id} y es del tipo int.</h1>'
    

#Ruta con parametro Float
@app.route('/float/<float:valor>')
def parametro_float(valor):
    '''
    Muestra el valor flotante de la URL 
    Args:
        valor: valor flotante.
    
    Returns:
        str: mensaje con el valor flotante del URL.

    Example:
        URL: /float/13.14159
    
    Resultado:
        El valor float del URL es 13.14159
    '''
    return f' <h1> El valor float del URL es {valor}</h1>'


#Ruta con parametro Path
#La diferencia con string es que path puede capturar datos despues de usar '/', mientras que el string no.
@app.route('/path/<path:ruta>')
def parametro_path(ruta):
    '''
    Muestra el Path capturado de la URL
    Args:
        ruta: ruta capturada.
    
    Returns:
        str: mensaje con el path del url

    Example:
        URL: /path/archivos/documentos/2026/path.txt
    
    Resultado:
        La ruta capturada del URL es archivos/documentos/2026/path.txt
    '''
    return f'<h1> La ruta capturada del URL es {ruta}</h1>'


#Ruta con parametro UUID (Identificador Unico Universal)/(Universally Unique Identifier).
#Es una cadena de 32 caracteres hexadecimales, normalmente representada en bloques separados por guiones:
#Ejemplo: 550e8400-e29b-41d4-a716-446655440000
#Usado para identificar recursos de manera unica como sesiones, usuarios, transacciones, etc.
@app.route('/uuid/<uuid:token>')
def parametro_uuid(token):
    '''
    Muestra el uuid capturado en la URL, si no es valido mostrara un error 404.

    Args:
        token: Identificador unico universal (uuid).
    
    Returns:
        str: mensaje con el uuid capturado.
    
    Example:
        URL: /uuid/550e8400-e29b-41d4-a716-446655440000
    
    Resultado:
        El UUID capturado es: 550e8400-e29b-41d4-a716-446655440000
    '''
    return f' <h1>El UUID capturado es: {token}'


if __name__=='__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')