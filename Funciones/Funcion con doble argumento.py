def mensaje(cantidad, palabra):       #Se agregan 2 argumentos: cantidad y palabra
    print("ingresa", cantidad, palabra)   #Cuerpo de la funcion


mensaje(5, "chetos")   #Se invoca la funcion y se declaran los 2 argumentos
# Salida = Ingresa 5 chetos

mensaje(2, "monedas")
# Salida = ingresa 2 monedas

cantidad = int(input("ingresa una cantidad: "))
palabra = input("ingrese de que: ")
mensaje(cantidad, palabra)
