from pathlib import Path
ruta = Path('C:/Users/danie/Documents/ProgramasPython/Manipulacion Archivos/Modulo OS/Carpeta')

#El metodo '.glob()' nos permite buscar archivos con un patron de busqueda
#El patron de busqueda se usa con la sintaxis de la siguiente manera:

# .glob('*.txt') para buscar archivos en una carpeta de una ruta especifica.
print("\n .glob('*.txt')")
for archivo in ruta.glob('*.txt'):
   print(archivo.name)  #Si no se pone el metodo '.name' se imprime la ruta completa

# .glob('**/*.txt') Para buscar archivos en todas las carpetas a partir de una ruta especifica.
print("\n .glob('**/*.txt')")
for archivos in ruta.glob('**/*.txt'):
    print(archivos.name)

# Para buscar las carpetas a partir de una ruta especifica.
print("\n .glob('*') usando .is_dir()")
for carpeta in ruta.glob('*'):
    if carpeta.is_dir():    #Si es un directorio
        print(carpeta.name)

# Para buscar las carpetas y subcarpetas a partir de una ruta especifica.
print("\n .glob('**/*') usando .is_dir()")
for carpeta in ruta.glob('**/*'):
    if carpeta.is_dir():    #Si es un directorio
        print(carpeta.name)