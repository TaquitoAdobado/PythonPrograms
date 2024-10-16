#Las tuplas son secuencias inmutables, NO pueden editarse despues de crearse dentro del programa con instrucciones como append.

inmutable_tuple = (8, 7, 6, 5, 4)

inmutable_tuple.append(3) #No se puede agregar elementos
#AttributeError: 'tuple' object has no attribute 'append'

del inmutable_tuple[3]  #No se puede eliminar elementos
#TypeError: 'tuple' object doesn't support item deletion

inmutable_tuple[0]= 9   #No se pueden editar elementos de la tupla
#TypeError: 'tuple' object does not support item assignment


#Salida: #AttributeError: 'tuple' object has no attribute 'append'
#Para ver el resto de errores, ponga # al inicio de las instrucciones anteriores