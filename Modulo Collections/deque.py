''' deque = double ended queue // en espanol: cola doblemente terminada
    Lista de alto nivel que permite agregar y quitar elementos de ambos lados. '''

from collections import deque

#Crear una deque
d = deque("hola")
print(d)    #Salida: deque(['h', 'o', 'l', 'a'])

#Eliminar elementos{

d.pop()     #Elimina el ultimo elemento al igual que en una lista
print(d)    #Salida: deque(['h', 'o', 'l'])

d.popleft() #Elimina el primer elemento a la izquierda
print(d)    #Salida: deque(['o', 'l'])

d.clear()   #Elimina todos los elementos
print(d)    #Salida: deque([])

#Agregar elementos

d.append("hola")    #Se agrega un elemento a la derecha como en una lista
print(d)            #Salida: deque(['hola'])

#extend agrega elementos iterables

d.extend("123") #Se iteró sobre el string "123" y se agregó cada elemento a la derecha
print(d)    #Salida: deque(['hola', '1', '2', '3'])

d.extend([1,2,3])   #Se iteró sobre la lista [1,2,3] y se agrego cada elemento a la derecha
print(d)    #Salida: deque(['hola', '1', '2', '3', 1, 2, 3])

#extendleft agrega elementos iterables a la izquierda

d.extendleft("hey") #Se itera sobre cada elemento del string y se van agregando a la izquierda
print(d)    #Salida: deque(['y', 'e', 'h', 'hola', '1', '2', '3', 1, 2, 3])


''' hacemos un clear para no tener tantos elementos en la cola y poder seguir haciendo pruebas '''
d.clear()
''' agregamos elementos a la derecha para continuar con las pruebas '''
d.extend("12345")
print(d)    #Salida: deque(['1', '2', '3', '4', '5'])


#rotate // recorre los elementos de la deque la cantidad de espacios que se le indique

#Si se indica un valor positivo, los elementos se desplazan hacia la derecha, (el ultimo se pasa al principio)
d.rotate(1)
print(d)    #Salida: deque(['5', '1', '2', '3', '4'])
''' Si se hubiera hecho d.rotate(2), el resultado seria: deque(['4', '5', '1', '2', '3']) '''

#Si se indica un numero negativo, los elementos se desplazan hacia la izquierda
d.rotate(-1)
print(d)    #Salida: deque(['1', '2', '3', '4', '5'])

#reverse // invierte los elementos de la deque
d.reverse()
print(d)    #Salida: deque(['5', '4', '3', '2', '1'])



''' Por ultimo, al crear una deque podemos usar el atributo maxlen para limitar el numero de elementos
que puede tener la deque. En caso de superar ese numero, se elimina el primer elemento de la cola. '''

nuevo_deque = deque("hola", maxlen = 4) #Se crea una deque con el string "hola" y se le asigna un maxlen de 4
print(nuevo_deque)  #Salida: deque(['h', 'o', 'l', 'a'])

nuevo_deque.extend("12")    #Se agregan los elementos "1" y "2" a la derecha
print(nuevo_deque)  #Salida: deque(['l', 'a', '1', '2'])
'''Como la longitud maxima es 4 y se estan agregando 2 elementos, primero se eliminan los 2 primeros elementos
luego se agregan los nuevos elementos iterados a la derecha'''


''' Cuando se sobrepasa el maxlen usando extendleft, primero se eliminan los ultimos elementos(a la derecha)
luego se agregan los nuevos elementos iterados a la izquierda '''
nuevo_deque2 = deque("hola", maxlen = 4)

nuevo_deque2.extendleft("21")
print(nuevo_deque2) #Salida: deque(['1','2','h','o'])

