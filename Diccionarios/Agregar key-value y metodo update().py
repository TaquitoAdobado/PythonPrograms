#Para agregar una key:value, se tiene que asignar un valor a una key que no exista, como si quisieras modificarlo.

dictionary = {"happy":"feliz", "sad":"triste", "angry":"enojado"}
print (dictionary)
#Salida: {'happy': 'feliz', 'sad': 'triste', 'angry': 'enojado'}

dictionary["bored"]= "aburrido"     #Como "bored" no se encuentra en el diccionario, se agregará con su value "aburrido"
print(dictionary)
#Salida: {'happy': 'feliz', 'sad': 'triste', 'angry': 'enojado', 'bored': 'aburrido'}

#Otra manera de agregar una key:value se usa el metodo .update({key:value})

dictionary.update({"anxious":"ansioso"})
print(dictionary)
#Salida: {'happy': 'feliz', 'sad': 'triste', 'angry': 'enojado', 'bored': 'aburrido', 'anxious': 'ansioso'}

