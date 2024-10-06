my_list = []    #Creamos una lista vacia para que el usiario la llene
swapped = True
cantidad_numeros = int(input("Cuantos numeros desea ordenar: "))    #Indicamos cuantos numeros tendremos en la lista

for i in range(cantidad_numeros):   #Repetimos este proceso el numero de veces indicado
    numeros = float(input("ingresa numero a la lista para ordenar: "))  #Ingresamos un numero
    my_list.append(numeros)     #ingresamos ese numero a la lista

while swapped:
    swapped = False
    for i in range(len(my_list)-1):
        if my_list[i] > my_list[i+1]:
            my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
            swapped = True
print ("Aquí están sus", len(my_list), "numeros ordenados de menor a mayor: ", my_list, end=" ")
