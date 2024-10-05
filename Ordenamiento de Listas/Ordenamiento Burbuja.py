#En este ordenamiento se hace una comparacion entre numeros adyacentes para luego intercambiar posiciones.

my_list = [8, 10, 6, 2, 4]          # Lista a ordenar de menor a mayor
swapped = True #Se necesita True para ingresar al bucle while

while swapped:
    swapped = False #No hay intercambios hasta ahora
    for i in range(len(my_list)-1):     # Necesitamos realizar 5-1 comparaciones (espacios entre los numeros de mi lista)
        if my_list[i] > my_list[i+1]:   # Comparamos elementos adyacentes
            swapped = True #Ocurre un intercambio
            my_list[i], my_list[i+1] = my_list[i+1], my_list[i]     #intercambiamos posiciones si se cumple condicion
print(my_list)