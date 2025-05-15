#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.


numbers = [1, 2, 3, 4]
target = 5
num_dict = {}

#num1 + num2 = target
#El enfoque para resolver esto es encontrar el num2 recorriendo el array con un bucle for sabiendo: num2 = target - num1
    #Usaremos como num1 el valor del array en la posicion de la iteracion actual
        #Si el cálculo no se encuentra en el diccionario, se agrega num1 como KEY
            #y como VALUE su posicion, o sea la itereacion actual

#En el momento en que el cálculo si se encuentre en el diccionario, significa que:
    #num2 = iteracion actual, representando el valor que se encuentre en su posicion del array
    #num1 = Value de la key que se encuentra en el diccionario. Representando el valor del array en la posicion
        #que se encuentra en el array


def twosum(numbers, target):
    for n in range(len(numbers)):
        if not target - numbers[n] in num_dict:
            num_dict[numbers[n]] = n  #num1 : posicion
        else:
            print([num_dict[target - numbers[n]], n]) #posicion_num1, posicion_num2
            break
twosum(numbers, target)

#Tambien podria hacerse con la siguiente sintaxis:
num_dict_2 = {} #usamos otro dict para no afectar al anterior

def twosum_2(numbers, target):
    for n in numbers:
        if not target - n in num_dict_2:
            num_dict_2[n] = numbers.index(n)
        else:
            print([num_dict_2[target - n], numbers.index(n)]) #posicion_num1, posicion_num2
            break
twosum_2(numbers, target)

