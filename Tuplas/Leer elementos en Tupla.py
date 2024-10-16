#Los elementos en una tupla pueden ser leidos de la misma manera que con una lista.

my_tuple = (1, 2, "hi", 3, 3.5, 4)

print(my_tuple[0])  #Salida = 1 
print(my_tuple[-1]) #Salida = 4
print(my_tuple[1:]) #Salida = (2, hi, 3, 3.5, 4)
print(my_tuple[:-2])#Salida = (1, 2, hi, 3)

for element in my_tuple:
    print(element)
#1ra iteracion: 1
#2da iteracion: 2
#3ra iteracion: hi
#4ta iteracion: 3
#5ta iteracion: 3.5
#6ta iteracion: 4