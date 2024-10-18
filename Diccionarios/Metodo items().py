#El metodo .items() es muy similar al metodo .keys()
#Sin embargo, a diferencia del .keys que crea una lista con todas las keys...
#El metodo .items() crea una LISTA DE TUPLAS donde cada tupla es un par de key:value

dictionary = {"one":"uno", "two":"dos", "three":"tres"}
print(dictionary.items())
#Salida: dict_items([('one', 'uno'), ('two', 'dos'), ('three', 'tres')])


for key, value in dictionary.items():
    print(key, "->", value)
    
