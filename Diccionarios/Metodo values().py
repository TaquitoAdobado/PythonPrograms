#Asi como se usa el metodo .keys() para devolver una lista con todas las key de un diccionario.
#El metodo .values() regresa una lista con todos los value de un diccionario.

dictionary = {"monday":"lunes", "tuesday": "martes", "wednesday":"miercoles", "thursday":"jueves", "friday":"viernes", "saturday":"sabado", "sunday":"domingo"}
print(dictionary.values())
#Salida: dict_values(['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo'])

for value in dictionary.values():
    print(value)
#Salida:
# lunes
# martes
# miercoles
# jueves
# viernes
# sabado
# domingo

#Recordemos que python solo puede buscar el value de una key. Al no poderse buscar la key de un value dado, este metodo es muy limitado.