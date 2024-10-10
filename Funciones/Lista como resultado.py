#Una lista puede ser el resultado de una funcion.

def my_function(n):     #Se crea una funcion
    my_list = []
    for i in range(0, n):       #rango del 0 al argumento a definir cuando se invoca funcion. 
        my_list.insert(0,i)     #En cada iteracion, en la posicion 0 se agrega el valor de i
    return my_list              #Retornará la lista

print(my_function(3))   #Salida = [2,1,0] // la salida es my_list


