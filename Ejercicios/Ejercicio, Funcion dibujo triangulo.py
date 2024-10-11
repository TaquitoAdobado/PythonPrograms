def triangulo(tamaño, caracter):
    for i in range(tamaño+1):
        print(" "*(tamaño-i) + caracter*i)
triangulo(50,"* ")