''' defaultdict es una clase que nos permite crear valores predeterminados para un diccionario en caso de que
una clave solciitada no exista en el mismo. '''

from collections import defaultdict

diccionario = defaultdict(lambda:"no existe") #Se le pasa un valor por defecto a la key que no exista en el diccionario

diccionario["nombre"] = "Daniel" #Se le asigna un valor a la key "nombre"
print(diccionario["apellido"])  #Se imprime un valor de una key que no existe en el diccionario
#Salida: no existe // Se imprime el valor predeterminado en lugar de arrojar un error.
