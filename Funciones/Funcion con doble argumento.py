#FUNCIONES DE 2 ARGUMENTOS

def mensaje(cantidad, palabra):       #Se agregan 2 argumentos: cantidad y palabra
    print("ingresa", cantidad, palabra)   #Cuerpo de la funcion

#------------------------------------------------------------------------------
#Argumento posicional.
#------------------------------------------------------------------------------

mensaje(5, "chetos")   #Se invoca la funcion y se declaran los 2 argumentos por su posición en la función
# Salida = Ingresa 5 chetos

#------------------------------------------------------------------------------
#Argumento por palabra clave. cuando no importa el orden mientras declaremos los argumentos por su nombre
#------------------------------------------------------------------------------

mensaje(palabra="cervezas", cantidad=15)    #No importa el orden mientras declaremos los argumentos por su nombre
# Salida = ingresa 15 cervezas

#------------------------------------------------------------------------------
# Recordemos que tambien se pueden declarar los argumentos antes de invocar a la funcion
#------------------------------------------------------------------------------

cantidad = int(input("ingresa una cantidad: "))
palabra = input("ingrese de que: ")
mensaje(cantidad, palabra)
