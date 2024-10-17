#Los diccionarios son otro tipo de estructura. No son una secuencia. Si son mutables (Editables).
#Los diccionarios estan formados por pares de clave:valor (pair of key:value), separados por una ","
#Cada key debe ser UNICA, no es posible tener 2 key iguales
#Las claves son sensibles a las mayusculas y minusculas, Key != key
#Para crear un diccionario: 

dictionary = { "key": "value", "key_2": "value_2", "key_3": "value_3"}  #Diccionario con 3 pares de key:Value
print (dictionary)  #Salida: {'key': 'value', 'key_2': 'value_2', 'key_3': 'value_3'}

#Tanto las key como los value pueden ser string, int, float
dictionary_2 = {"string_key": 111, 222:"string_value", 444:5.5}
print(dictionary_2) #Salida: {'string_key': 111, 222: 'string_value', 444: 5.5}

#Tambien se pueden crear diccionarios vacios
empty_dictionary = {}
print (empty_dictionary)    #Salida= {}


#La funcion len() regresa la cantidad de pares key:value
print(len(dictionary))  #Salida = 3 // Se tienen 3 pares de key:value

