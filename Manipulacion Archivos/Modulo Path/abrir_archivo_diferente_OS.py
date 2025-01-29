''' Usamos el objeto Path para poder reconocer la sintaxis de las rutas de otros sistemas operativos.   '''
from pathlib import Path

#En Path agregamos una ruta con '/' el cual es usado en OS Mac y Linux
carpeta = Path('C:/Users/danie/Documents/ProgramasPython/Manipulacion Archivos/Modulo OS/Carpeta')

'''
El siguiente paso se puede omitir si el archivo se agrega directamente en la ruta almacenada en la variable 'carpeta':
    'C:/Users/danie/Documents/ProgramasPython/Manipulacion Archivos/Modulo OS/Carpeta/archivo.txt'
o si se agrega fuera de path() en la misma variable 'carpeta':
    carpeta = Path('C:/Users/danie/Documents/ProgramasPython/Manipulacion Archivos/Modulo OS/Carpeta') / 'archivo.txt'
'''
#Se indica el archivo que queremos usando la ruta almacenada en carpeta y añadiendo '/' + nombre del archivo
archivo = carpeta / 'archivo.txt'

#Probamos que el archivo se pueda abrir en nuestro OS Windows, aunque tenga la sintaxis de Mac/Linux.
#Abrimos y cerramos el archivo como usualmente se haria sin Path:
mi_archivo = open(archivo)
print(mi_archivo.read())
mi_archivo.close()