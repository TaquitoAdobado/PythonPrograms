''' El modulo time nos permite medir el tiempo de ejecucion de un programa
sintaxis:

import time
inicio = time.time()
Cuerpo del codigo
fin = time.time()
tiempo_ejecucion = fin - inicio '''

#Definamos 2 funciones para comparar el tiempo de ejecucion.
import time

def prueba_for(numero):
    lista = []
    for num in range(numero):
        lista.append(num)
    return lista

def prueba_while(numero):
    lista = []
    contador = 0
    while contador < numero:
        lista.append(contador)
        contador += 1
    return lista

#Llamamos a las funciones y medimos el tiempo de ejecucion


inicio_tiempo = time.time()
prueba_for(1000000) #un millón
fin_tiempo = time.time()
tiempo_ejecucion = fin_tiempo - inicio_tiempo
print(f' El tiempo de ejecucion con for es: {tiempo_ejecucion}')

inicio_tiempo = time.time()
prueba_while(1000000) #un millón
fin_tiempo = time.time()
tiempo_ejecucion = fin_tiempo - inicio_tiempo
print(f' El tiempo de ejecucion con while es: {tiempo_ejecucion}')


'''Cuando los tiempos de ejecucion son demasiado rapidos, el modulo time puede dar resultados incorrectos
Por lo que se recomienda usar el modulo timeit para medir tiempos de ejecucion.'''