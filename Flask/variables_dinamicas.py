#Una variable dinamica es aquella que puede cambiar su valor dependiendo de la entrada del usuario.
#Para poder usar variables dinamicas se utilizan los simbolos < >

from flask import Flask, render_template
app = Flask(__name__)


#Definimos una ruta dinamica.
#El valor que se use en <nombre> sera capturado y usado como parametro en la funcion.
@app.route('/saludo/<nombre>')
def saludo_nombre(nombre):
    ''' Muestra un saludo con el nombre proporcionado en la URL.

        Args:
            nombre (str): Nombre capturado en la ruta dinamica.

        Returns:
            str: Saludo personalizado.

        Example:
            URL: /saludo/Daniel
            Resultado: Bienvenido Daniel
    '''
    return f'<h1>Bienvenido {nombre}</h1>'


#Con un diccionario de usuarios creados (datos_usuarios) mostraremos la informacion de un usuario renderizando una plantilla HTML.
@app.route('/info/<usuario>')
def info_usuario(usuario):
    '''
    Muestra la informacion de un usuario proporcionando su nombre en la URL.

    Args:
        usuario (str): Nombre de usuario capturado en la URL.

    Returns:
        str: Informacion del usuario renderizada en una plantilla HTML.

    Usuarios registrados:
        - TaquitoAdobado
        - UsuarioFlask
        - ProgramadorPython

    Example:
        URL: /info/TaquitoAdobado
        Resultado:
            Nombre: Taquito
            Apellido: Adobado
            Edad: 31
            Sexo: Masculino
    '''
    # Guardamos el nombre de usuario tal cual fue capturado para usarlo en mensajes de error.
    usuario_crudo = usuario
    # Normalizamos el nombre a minusculas para buscar en el diccionario.
    usuario = usuario.lower() 
    # Obtenemos los datos del nombre de usuario capturado en la URL.
    datos = datos_usuarios.get(usuario)
    #Si el usuario existe, renderizamos la plantilla con sus datos.
    if datos:
        return render_template('info_usuario.html', usuario = datos)
        #usuario=datos: usuario ahora es el diccionario con los datos del usuario.
        
    #Si el usuario no existe, mostramos un mensaje de error.
    else:
        #Usamos usuario_crudo para mostrar el nombre tal cual fue capturado.
        return f'<h1><span style="color:red">ERROR:</span>Usuario {usuario_crudo} no registrado.</h1>'
    
    #NOTA: Asegurarse de tener la plantilla info_usuario.html en la carpeta templates.
    


#Diccionario con datos de usuarios.
datos_usuarios = {
    'taquitoadobado': {
        'username': 'TaquitoAdobado',
        'nombre': 'Taquito',
        'apellido': 'Adobado',
        'edad': 31,
        'sexo': 'Masculino' },
    'usuarioflask': {
        'username': 'UsuarioFlask',
        'nombre': 'Alex',
        'apellido': 'Mundo',
        'edad': 32,
        'sexo': 'Masculino'},
    'programadorpython': {
        'username': 'ProgramadorPython',
        'nombre': 'Carla',
        'apellido': 'Juaneza',
        'edad': 32,
        'sexo': 'Femenino'}
    }


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')