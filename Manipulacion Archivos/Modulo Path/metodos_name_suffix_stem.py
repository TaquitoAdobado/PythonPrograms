'''En este script se explicará loq ue hacen los metodos .name , .suffix y .stem del modulo pathlib
para objetos tipo Path'''

from pathlib import Path
archivo = Path('C:/Users/danie/Documents/ProgramasPython/Manipulacion Archivos/Modulo OS/Carpeta/archivo.txt')

#   Metodo '.name'
'''El metodo '.name' nos devolverá el nombre del archivo con su extension incluida'''
print(archivo.name)

#   Metodo '.suffix'
'''El metodo '.suffix' nos devolverá unicamente la extension del archivo seleccionado'''
print(archivo.suffix)

#   Metodo '.sufix'
'''El metodo '.sufix' nos devolverá unicamente la extension del archivo seleccionado'''

#   Metodo '.stem'
'''El metodo '.stem' nos devolverá unicamente el nombre del archivo sin extension'''
print(archivo.stem)