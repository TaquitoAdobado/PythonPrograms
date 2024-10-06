#Para realizar una copia del contenido de una lista usamos [:]

my_list1 = [1, 2, 3, 4]  #Creamos una lista
my_list2 = my_list1[:]   #Creamos una copia del contenido de my_list1 en my_list1. 
                         #la cual es independiente de my_list1 ya que está almacenado en un lugar diferente

my_list1[0] = 5     #Cambiamos el valor de la posicion 0 de la lista 1 por un 5
print(my_list2)     #Imprimimos la lista 2 y el cambio anterior no tendria porque afectar su contenido
print(my_list1)     #Imprimimos la lista 1 y aqui si se tiene que ver reflejado el cambio


