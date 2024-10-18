#Una tupla es una secuencia inmutable (No puede editarse)
#Cada elemento en una tupla puede ser de distinto tipo, como int, float y string

#Se crea igual que una lista pero usando () en lugar de []

tuple_1 = (1,2,4,8)

# o simplemente separando los valores con ,

tuple_2 = 1., .5, .25, "hi"

#Una tupla puede crearse vacia

tuple_3 =()

#Se puede crear una tupla de un solo elemento, pero se debe agregar una "," al final para distinguirse de un valor ordinario

tuple_4 = (5,) #Si quitamos la , tuple_4 = 5, no será una tupla, sera un valor asignado a una variable.
#-------------------------------------------------------------------------------
print(tuple_1)  #Salida: (1, 2, 4, 8)
print(tuple_2)  #Salida: (1.0, 0.5, 0.25, 'hi')
print(tuple_3)  #Salida: ()
print(tuple_4)  #Salida: (5,)
#-------------------------------------------------------------------------------


