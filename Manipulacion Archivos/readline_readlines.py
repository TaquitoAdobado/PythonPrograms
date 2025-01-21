mi_archivo1 = open('prueba.txt')
'''
Con el metodo .readlines() podemos almacenar en una variable todos los renglones del archivo en formato de lista.
'''
lista_renglones = mi_archivo1.readlines()
print(type(lista_renglones))
print(lista_renglones)

'''
Al ser de tipo lista, podemos usar todos los métodos y atributos de las listas.
'''
print("\n3er renglon: ", lista_renglones[2])  # Se imprimirá el renglon 3

'''
El metodo 'readline()' asignado a una variable posiciona el cursor en la primer linea (el primer renglon) 
del archivo de texto (si no se ha movido previamente).
En este caso se crea una nueva variable para que el cursor esté en el inicio del archivo (primer renglon).
'''
mi_archivo2 = open('prueba.txt')
mi_renglon = mi_archivo2.readline()
print("\n1er renglon: ", mi_renglon)

'''
Si se vuelve a usar el metodo readline() sobre la misma variable, el cursor se posicionará en la linea siguiente
(el segundo renglon).
'''
mi_renglon = mi_archivo2.readline()
print("2do renglon: ", mi_renglon)

# Es buena práctica cerrar los archivos después de usarlos
mi_archivo1.close()
mi_archivo2.close()
