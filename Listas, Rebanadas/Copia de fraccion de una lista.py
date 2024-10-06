# Se puede usar [start:end] para copiar una fraccion de una lista de la siguiente manera
#Donde star es la posicion desde donde se copiara y end sera la ultima posicion -1 a copiar.

my_list1 = [1, 2, 3, 4, 5]  #Primero creamos una lista
my_list2 = my_list1[1:4]    #Copiamos la lista desde la posicion 1 (el numero 2), hasta la posicion 4-1 (el numero 4)
print(my_list2)     #El resultado debe ser del numero 2 hasta el numero 4

#Si omitimos el start, se copiará desde la posición 0
my_list3 = my_list1[:4]
print(my_list3)     #El resultado debe ser desde el numero 1 hasta el 4

#Si omitimos el end, se copiará hasta el ultimo valor de la lista, lo que es lo mismo que len(my_list1)
my_list4 = my_list1[1:]
print(my_list4)     #El resultado debe ser desde el numero 2 hasta el numero 5