'''Cuando abrimos un archivo con open(), si no se especifica el modo de apetura, por defecto será
en modo lectura (r).'''
mi_archivo = open('prueba.txt','r') # == mi_archivo = open('prueba.txt')
'''Cuando un archivo se abre en modo lectura, no se puede editar.'''
mi_archivo.close()

'''Para poder editar un archivo es necesario abrirlo en modo escritura
Hay 2 formas de abrir un archivo en modo escritura, la primera es usando (w)
La primera forma es abrirlo con (w)
Si el archivo no existe SE CREARÁ.
Si el archivo si existe SE ELIMINARÁ TODO SU CONTENIDO para poder editarlo'''

mi_archivo_2 = open('prueba2.txt','w') #Se crea archivo prueba2.txt
''' Para editar el archivo usaremos el metodo '.write()  '''
mi_archivo_2.write("Hola Mundo")
mi_archivo_2.close()

''' La segunda forma es abrirlo con (a)
Al usar (a), el contenido del archivo permanecerá intacto y el cursor se posicionará al final del archivo,
despues del ultimo caracter. De esta forma si agregamos algo al archivo, se agregará despues del contenido existente.    '''

mi_archivo_2 = open('prueba2.txt','a')
mi_archivo_2.write("\nEstoy debajo de Hola Mundo")
mi_archivo_2.close()