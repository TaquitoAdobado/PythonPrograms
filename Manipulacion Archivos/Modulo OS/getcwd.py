#El modulo os permite interactuar con el sistema operativo usando sus diferentes metodos.
import os

# os.getcwd (Get Current Work Directory)
'''como su nombre lo indica, este metodo sirve para obtener la ruta actual desde donde se ejecuta el script'''
ruta = os.getcwd()
print(ruta) # en mi caso C:\Users\danie\Documents\ProgramasPython\Manipulacion Archivos\Modulo OS



''' C:\\Users\\danie\\Documents\\ProgramasPython\\Manipulacion Archivos\\Modulo OS\\Carpeta\\archivo.txt
Una ruta puede tener 2 elementos:

*   El nombre de base: El camino hasta llegar a donde se encuentra tu archivo.
C:\\Users\\danie\\Documents\\ProgramasPython\\Manipulacion Archivos\\Modulo OS\\Carpeta
*   El nombre del archivo:
archivo.txt   '''

