#El metodo '.relative_to()' nos permite obtener la ruta relativa a una ruta especifica
#En otras palabras, nos muestra una ruta a partir de un punto especificado.

from pathlib import Path

ruta = Path('C:/Users/danie/Documents/ProgramasPython/Manipulacion Archivos/Modulo OS/Carpeta/archivo.txt')
desde_documents = ruta.relative_to(Path('C:/Users/danie/Documents'))
desde_modulo_os = ruta.relative_to(Path('C:/Users/danie/Documents/ProgramasPython/Manipulacion Archivos/Modulo OS'))
print("\nruta completa:\n",ruta)
print("\nruta despues de Documents:\n",desde_documents)
print("\nruta despues de Modulo OS:\n",desde_modulo_os)
