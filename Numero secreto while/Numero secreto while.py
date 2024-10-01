secret_number = 777
variable = False

print(
"""
+================================+
| ¡Bienvenido a mi juego!        |
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
| Pista: son 3 y dan suerte      |
+================================+
""")

while variable == False:
    try:
        numero = int(input("ingrese tu numero: "))
        
        if numero == secret_number:
            print("¡Bien hecho! Eres libre ahora.")
            variable = True
        
        else:
            print("Numero equivocado ¡Ja, ja! ¡Estás atrapado en mi bucle!")
        
    except ValueError:
                print ("Eso NO es un numero ¡MUAJAJAJA!")
