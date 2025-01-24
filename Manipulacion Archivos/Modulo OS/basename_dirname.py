import os

# Una ruta puede tener 2 elementos:

ruta = 'C:\\Users\\danie\\Documents\\ProgramasPython\\Manipulacion Archivos\\Modulo OS\\Carpeta\\archivo.txt'

'''
*   El dirname: Es la ruta del directorio que contiene el archivo.
C:\\Users\\danie\\Documents\\ProgramasPython\\Manipulacion Archivos\\Modulo OS\\Carpeta'''
dirname = os.path.dirname(ruta)
print(dirname)

'''
*   El basename: Es el nombre del archivo sin incluir el directorio
archivo.txt   '''
basename = os.path.basename(ruta)
print(basename)

