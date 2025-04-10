'''La clase Counter del modulo collections nos permite contar la cantidad de veces que aparece un elemento
ya sea dentro de un string como de una lista'''

mi_lista = [1,3,3,3,2,2,5,5,5,5,5,4,4,4,4]

#Formas comunes de contar los elementos repetidos de una lista
#Ejemplo 1
diccionario_1 = {i: mi_lista.count(i) for i in mi_lista}
print(diccionario_1)

#Ejemplo 2
diccionario_2 = {}
for numero in mi_lista:
    if numero in diccionario_2.keys():
        diccionario_2[numero] +=1
    else:
        diccionario_2[numero] = 1
print(diccionario_2)

#Usando Counter del modulo collections
from collections import Counter

#Counter usado en una lista
print(Counter(mi_lista))

#Counter usado en un string
print(Counter("mississippi"))

#Counter tiene distintos metodos que podemos usar como: most_common() que nos devuelve los elementos mas comunes

print(Counter(mi_lista).most_common())  #Si se indica sin argumentos, devuelve todos los elementos
print(Counter(mi_lista).most_common(2)) #Devuelve los dos elementos mas comunes




