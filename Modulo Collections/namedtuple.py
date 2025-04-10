''' namedtuple es una clase del modulo collection que nos permite crear tuplas con nombres de atributos
esto nos permite ademas de poder acceder a un valor de una tupla por su indice, hacerlo por su atributo'''

persona_1 = ("Daniel", 30, 1.70)
print(persona_1[1])  #Salida: 30

from collections import namedtuple

#Creamos un objeto de la clase namedtuple con el nombre de la tupla y una lista con los nombres de los atributos
Persona = namedtuple("Persona",["nombre", "edad", "altura"])

#Creamos una instancia de la tupla
daniel = Persona("Daniel", 30, 1.70)

print(daniel.nombre)  #Salida: Daniel
print(daniel.edad)    #Salida: 30
print(daniel.altura)  #Salida: 1.70

