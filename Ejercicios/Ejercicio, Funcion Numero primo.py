#Esta funcion devolverá True si un numero es primo o False si no lo es.
#Para que un numero sea primo debe der >1 y solo debe ser divisible entre 1 y entre si mismo.

def prime_number(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5)+1):
        if number%i == 0:
            return False
    return True
        
print(prime_number(11))