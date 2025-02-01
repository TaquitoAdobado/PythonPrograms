from pathlib import Path
carpeta = Path('C:/Users/danie/Documents/ProgramasPython/Manipulacion Archivos/Modulo OS/Carpeta')

#El metodo '.glob()' nos permite buscar archivos con un patron de busqueda
#El patron de busqueda se usa con la sintaxis de la siguiente manera:

# .glob('*.txt') para buscar archivos en una carpeta de una ruta especifica.
print("\n .glob('*.txt')")
for archivo in carpeta.glob('*.txt'):
   print(archivo)

# .glob('**/*.txt') Para buscar archivos en todas las carpetas a partir de una ruta especifica.
print("\n .glob('**/*.txt')")
for archivos in carpeta.glob('**/*.txt'):
    print(archivos)