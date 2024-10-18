#Si se desea obtener un valor especifico de un diccionario, se debe proporcionar su clave(key) entre corchetes []
# A diferencia de las listas, no se buscan los valores por su posicion

dictionary={"Dog": "Perro", "Cat": "Gato", "Turtle": "Tortuga"}     #Se crea el diccionario
print(dictionary["Dog"])    #Se busca el valor de la clave "Dog"
#Salida: Perro

# Se puede buscar el valor de una clave, Pero NO se puede buscar la clave de un valor

print(dictionary["Perro"])
#Salida: KeyError: 'Perro'
# El error es un keyerror ya que python busca claves (key), y no existe la key "Perro"

