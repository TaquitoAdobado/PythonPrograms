#Se puede agregar una lista como argumento de una funcion

def suma_lista(lista):  #Se crea funcion suma_lista con argumento que sera una lista mas adelante.
    s = 0
    for elemento in lista:      #Se realiza un For para realizar la suma de los numeros en la lista
        s += elemento
    return s               #el return devolverá el valor de la suma

print(suma_lista([1,2,3]))  #Hacemos print de la funcion para tener una salida y se añade una lista como argumento.
#Salida = 6