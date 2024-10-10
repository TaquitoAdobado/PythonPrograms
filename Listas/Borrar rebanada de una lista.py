#Para borrar un valor especifico de una lista usamos del

my_list1 = [1, 2, 3, 4]     #Creamos una lista

del my_list1[0]     #Eliminamos el valor de la posición 0 de la lista
print (my_list1)    #El resultado deberia ser 2, 3, 4

#Para borrar una rebanada de una lista indicamos [start:end] igual que cuando copiamos
my_list2 = [1, 2, 3, 4]
del my_list2[1:3]   #Eliminamos de la lista desde la posición 1 hasta la posición 3-1
print (my_list2)    #El resultado deberia ser 1, 4

#De igual manera, si no indicamos start, empezará desde posición 0
my_list3 = [1, 2, 3, 4]
del my_list3[:3]    #Eliminamos desde la posición 0 hasta la posicion 3-1
print (my_list3)    #El resultado deberia ser 4

#De igual manera, si no indicamos end, terminará hasta posición final, o sea, len(my_list4)
my_list4 = [1, 2, 3, 4]
del my_list4 [1:]   #Eliminamos desde la posicion 1 hasta la ultima posicion
print(my_list4)     #El resultado deberia ser 1

#Si queremos eliminar todo el contenido de una lista, no especificamos start ni end
my_list5 = [1, 2, 3, 4]
del my_list5[:]     #Eliminamos todo el contenido de la lista
print(my_list5)     #El resultado deberia ser la lista vacia, ya que todavia existe

#Si queremos eliminar una lista, no usaremos [:]
my_list6 = [1, 2, 3, 4]
del my_list6        #Eliminamos la lista my_list6
print(my_list6)     #Al hacer print saldrá error ya que no hay lista que pueda imprimir