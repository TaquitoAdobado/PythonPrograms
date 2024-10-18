#El metodo .keys() retorna una LISTA con todas las KEY de un diccionario

dictionary = {"monday":"lunes", "tuesday": "martes", "wednesday":"miercoles", "thursday":"jueves", "friday":"viernes", "saturday":"sabado", "sunday":"domingo"}
print(dictionary.keys())
#Salida: dict_keys(['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'])

#Al tener la lista con todas las claves, se puede acceder a todo el diccionario
for i in dictionary.keys():
    print(i, "->", dictionary[i])
#Salida:
# monday -> lunes
# tuesday -> martes
# wednesday -> miercoles
# thursday -> jueves
# friday -> viernes
# saturday -> sabado
# sunday -> domingo