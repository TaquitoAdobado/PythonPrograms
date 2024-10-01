# Contador de numeros pares e impares
# Haga un Loop en el que se deben ingresar numeros hasta que el usuario ingrese 0
# Cuando se ingrese 0 se debe hacer un recuento de numeros pares e impares
# Use funcion While

numero_par = 0
numero_impar = 0
variable = False  # Variable bandera para controlar el bucle

print("Contador de numeros pares e impares")

while variable == False:  # Mientras la bandera sea False, el bucle continúa
    try:
        numero = float(input("Ingrese un numero o ingrese el numero 0 para hacer el recuento: "))
        
        if numero == 0:
            variable = True  # Si el usuario ingresa 0, se cambia la bandera y el bucle termina
            
        elif numero % 2 != 0:
            numero_impar += 1
            
        else:
            numero_par += 1
            
    except ValueError:
        print("Ese no es un numero, por favor intente de nuevo, BABOSO.")

print("Cantidad de numeros pares: ", numero_par)
print("Cantidad de numeros impares: ", numero_impar)

