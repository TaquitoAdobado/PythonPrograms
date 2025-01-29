'''Con el metodo '.exists()' se nos devolverá un valor booleano para identificar si un archivo existe.
Esto puede ser aprovechado de maneras diferentes, en este ejemplo solo se imprimira un mensaje dependiendo
de si existe o no un archivo.'''

from pathlib import Path
archivo = Path('C:/Users/danie/Documents/ProgramasPython/Manipulacion Archivos/Modulo OS/Carpeta/archivo.txt')

if archivo.exists():
    print("El archivo si existe")
else:
    print("El archivo no existe")