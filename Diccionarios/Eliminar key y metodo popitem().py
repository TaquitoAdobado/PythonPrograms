#Si se elimina una key tambien se eliminará su value, recordemos que una key viene en conjunto con su value. key:value

#Para eliminar una key se puede usar la instruccion "del"

dictionary={"cat":"gato", "dog":"perro", "ghost":"fantasma"}    #Creamos un diccionario
print (dictionary)  #Salida: {'cat': 'gato', 'dog': 'perro', 'ghost': 'fantasma'}

del dictionary["ghost"] #Eliminamos la key "ghost" con todo y su value
print(dictionary)   #Salida: {'cat': 'gato', 'dog': 'perro'}

#Otra manera de eliminar una key es usando el metodo .popitem()
#   .popitem() eliminará la ultima key del diccionario. 
#En versiones anteriores a la 3.6.7 de python, se eliminará un key al azar, ya que los diccionarios se crean con un orden aleatorio.

dictionary.popitem()
print(dictionary)   #Salida: {'cat': 'gato'}
