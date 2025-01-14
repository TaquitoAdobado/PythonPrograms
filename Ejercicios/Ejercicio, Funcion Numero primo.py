""" Esta función devolverá si un número ingresado es primo.
Además, mostrará el conteo de cuantos números primos hay hasta el número ingresado
y para finalizar mostrará la lista de todos esos números.
#Para que un número sea primo debe der >1 y solo debe ser divisible entre 1 y entre sí mismo.
#Consejo, después del 2, un número primo no puede ser par. """


def prime_number(number):
    # Si es menor a 2 no puede ser un número primo.
    if number < 2:
        print(f"{number} no es un número primo")
        return

    # Se crea lista donde almacenaremos los números primos. Incluimos 2 ya que será el mínimo permitible.
    primos = [2]
    iteracion = 3

    # Bucle while para iterar desde 3 hasta el número ingresado
    while iteracion <= number:
        # Bucle for para verificar si 'iteracion' es divisible por algún número impar menor que 'iteracion'
        for n in range(3, iteracion, 2):
            if iteracion % n == 0:
                # Si 'iteracion' es divisible por 'n', no es primo, incrementa iteracion y rompe el bucle for
                iteracion += 2
                break
        else:
            # Si no se encuentra divisor, 'iteracion' es un número primo, se añade a la lista
            primos.append(iteracion)
            iteracion += 2

    # Indicará cuántos números primos hay hasta el número ingresado
    list_count = len(primos)
    print(f"El número {number} sí es un número primo")
    print(f"La cantidad de números primos hasta el número ingresado es: {list_count}")
    print(f"La lista de números primos hasta el número ingresado es:\n{primos}")

#El usuario ingresará un numero para activar la función
while True:
    try:
        number=int(input("Insert a number: "))
        break
    except ValueError:
        print("Ingrese un numero valido")
#Se invoca a la funcion
prime_number(number)