#Ya sabemos que un diccionario se crea de la sig manera.

dictionary = {"key":"value", "key_2":"value_2", "key_3":"value_3"}

#Sin embargo otra manera de crearlo es alinearlo de manera vertical para hacerlo mas legible en caso de tener una expresion grande o larga.

vertical_dictionary = {
    "new_key": "new_value",     #No olvides poner una "," si escribirás otra key
    "new_key2": "new_value2",
    "new_key3": "new_value3"
}

print(dictionary)   #Salida: {'key': 'value', 'key_2': 'value_2', 'key_3': 'value_3'}
print(vertical_dictionary)  #Salida: {'new_key': 'new_value', 'new_key2': 'new_value2', 'new_key3': 'new_value3'}

#La manera en la que creemos el diccionario no afectará la forma en la que salga en el print.