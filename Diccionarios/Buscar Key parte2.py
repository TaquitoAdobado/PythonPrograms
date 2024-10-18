#Para saber si una key se encuentra dentro un diccionario, se hace uso del in y not in, asi mismo de las listas.

dictionary = {"water":"agua", "fire":"fuego", "thunder":"trueno"}    #Se crea un diccionario

my_list = ["water", "earth", "ice", "fire", "wind", "agua", "thunder"]  #Se crea una lista con las claves a buscar en mi diccionario

for key in my_list: #Para cada valor en my_list
    if key in dictionary:   #Si la key se encuentra en dictionary. // Podria usarse not in para buscar lo que no esté en el diccionario.
        print(key, "->", "Si está")
    else:
        print(key, "->", "No está")

# Salida: 
# water -> Si está
# earth -> No está
# ice -> No está
# fire -> Si está
# wind -> No está
# agua -> No está   // agua la marca como "No está" porque python solo busca claves(key) no valores(value). {Key:Value}
# thunder -> Si está
