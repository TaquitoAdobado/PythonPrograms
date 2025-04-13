''' El modulo timeit nos permite medir el tiempo de ejecucion de un programa al igual que el modulo time.
sin embargo de manera mas precisa para tiempos de ejecucion mas cortos (<1s).'''

import timeit   #Se tiene que importar el modulo timeit

# tiempo_ejecucion = timeit.timeit(stmt, setup, number)

#stmt : statement es la llamada a la funcion, debe estar escrita entre docstring (''' ''') y alamcenado en una variable
#setup: Funcion a medir el tiempo, debe estar escrita entre docstring (''' ''') y alamcenado en una variable
#number: Numero de veces que se ejecutara la funcion


stmt_for = ''' 
prueba_for(10) 
'''

setup_for = '''
def prueba_for(numero):
    lista = []
    for num in range(numero):
        lista.append(num)
    return lista
'''


tiempo_ejecucion = timeit.timeit(stmt_for, setup_for, number = 100000)
print(f' El tiempo de ejecucion con for es: {tiempo_ejecucion}')
