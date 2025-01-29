from pathlib import Path
'''Como Path es un objeto de tipo Path(), podemos usar el metodo '.read_text()' con el cual
ya no es necesario hacer un open() ni un .close() del archivo'''

archivo_2 = Path('C:/Users/danie/Documents/ProgramasPython/Manipulacion Archivos/Modulo OS/Carpeta/archivo.txt')
print(archivo_2.read_text())