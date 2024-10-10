#con el operador "in" podemos verificar si el elemento (a la izquierda del in)
#se encuentra en la lista (a la derecha del in)

my_list = [1, 2, 3, 4, 5]   #Creamos una lista
5 in my_list    #Verifica si el numero 5 esta dentro de la lista my_list
#Por si solo no devuelve ningun resultado, pero si colocamos un print(), devolverá True si la verificacion es correcta
#De lo contrario, devolverá False

print(5 in my_list)     #Resultado debe ser True

#con el operador "not in" podemos verificar si el elemento (a la izquierda del not in)
#se encuentra ausente en la lista (a la derecha del not in)

my_list2 = [1, 2, 3, 4, 5]  #Creamos la lista
print(6 not in my_list2)    #Como 6 no se encuentra dentro de la lista, la verificacion fue exitosa y devolverá True
print(5 not in my_list2)    #Como 5 si se encuentra dentro de la lista, la verificacion no fue exitosa y devolverá False