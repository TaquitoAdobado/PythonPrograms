print("Identificador de palindromos")   #Titulo del programa mostrado al usuario
frase = input("ingrese su palabra o frase: ", )#Se ingresa una palabra o frase por el usuario
frase_nueva = "".join(frase.split()).lower()  #Se divide frase en palabras, se juntan sin espacio y se convierten a minucula
palindromo = frase_nueva==frase_nueva[::-1]  #Se crea un flag True o False si frase_sin espacio = frase_sin_espacio alrevez
if palindromo:      #Si palindromo es True
    print(f"La palabra o frase '{frase}' \nSI es un palindromo") #Si es True se imprime esta primera linea
else:               #Si palindromo es Fale
    print(f"La palabra o frase '{frase}' \nNO es un palindromo")  #Si es False se imprime esta segunda linea