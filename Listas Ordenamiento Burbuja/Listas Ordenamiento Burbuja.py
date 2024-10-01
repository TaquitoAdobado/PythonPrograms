#Listas
#Ordenamiento Burbuja

my_list = [8, 10, 6, 2, 4] #Se crea la lista

for i in range(len(my_list) -1): #se necesitan 5 comparaciones
    if my_list[i] > my_list[i + 1]: #Comparamos elementos adyacentes
        my_list[i] , my_list[i + 1] = my_list[i + 1] , my_list[i] #Intercambiamos elementos
        
print(my_list)
