"""Para abrir un archivo desde Python, sin indicar la ruta, se debe tener ese archivo en la misma carpeta que el script.
    En este caso se tiene el archivo 'prueba.txt' """

mi_archivo = open('prueba.txt')
"""Se aloja el archivo en una variable con el método 'open()' 
    indicando el nombre del archivo dentro de los parentesis.
    
Como la variable 'mi_archivo' contiene un archivo, ahora tiene una serie de metodos asociados a ese tipo de archivos.
Antes de poder abrir un archivo con 'print()' se tiene que usar el metodo '.read()' para leer el contenido de este."""
print(mi_archivo.read())

"""Siempre que se trabaje con la apertura de un archivo, no olvidar hacer el cierre del mismo al final"""
#mi_archivo.close()



