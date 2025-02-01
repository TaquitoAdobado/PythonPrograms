#El metodo '.parent' nos devuelve la ruta de la carpeta padre del archivo seleccionado
#Llamese carpeta padre a la carpeta final que se encuentra en la ruta

from pathlib import Path
archivo = Path('C:/Users/danie/Documents/ProgramasPython/Manipulacion Archivos/Modulo OS/Carpeta/archivo.txt')
print(archivo.parent)

#se puede acumular el metodo '.parent' para obtener la ruta de la carpeta anterior a la carpeta padre.
print(archivo.parent.parent)
print(archivo.parent.parent.parent)
print(archivo.parent.parent.parent.parent)