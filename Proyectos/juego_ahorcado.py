from random import choice

lista_palabras = ["slime","dragon","espada","escudo","taberna","guerrero"]
intentos = 9
letras_correctas = []
letras_usadas = []
juego_continua = True


def eleccion_palabra(lista_palabras):
    palabra_elegida = choice(lista_palabras)
    letras_unicas = set(palabra_elegida)

    return palabra_elegida, letras_unicas


def pedir_letra():
    abecedario = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,ñ,o,p,q,r,s,t,u,v,w,x,y,z"

    while True:
        letra_elegida = input("Ingresa una letra: ")
        if len(letra_elegida) == 1 and letra_elegida in abecedario and letra_elegida not in letras_usadas:
            letras_usadas.append(letra_elegida)
            break
        elif letra_elegida in letras_usadas:
            print("Ya has usado esa letra. Intenta otra.")
        else:
            print("Letra invalida, intenta otra.")

    return letra_elegida, letras_usadas,


def revision_letra(letra_elegida, palabra_elegida, intentos, letras_correctas):
    if letra_elegida in palabra_elegida:
        letras_correctas.append(letra_elegida)
    else:
        intentos -= 1
        print("Te quedan: ", intentos, "intentos ")

    return intentos, letras_correctas


def ganar():
    print("\nEnhorabuena, haz ganado!")
    return False


def perder(palabra_elegida):
    print("\nGame Over!!!")
    return False


def tablero(palabra_elegida, letras_correctas):
    palabra_oculta = []
    print("-"*20)
    for letra in palabra_elegida:
        if letra in letras_correctas:
            palabra_oculta.append(letra)
        else:
            palabra_oculta.append("-")
    print(" ".join(palabra_oculta))


palabra_elegida, letras_unicas = eleccion_palabra(lista_palabras)
while juego_continua == True:
    tablero(palabra_elegida, letras_correctas)
    letra_elegida, letras_usadas = pedir_letra()
    intentos, letras_correctas = revision_letra(letra_elegida, palabra_elegida, intentos, letras_correctas)
    if len(letras_correctas) == len(letras_unicas):
        juego_continua = ganar()
    elif intentos == 0:
        juego_continua = perder(palabra_elegida)
print("La palabra oculta era: "," ".join(palabra_elegida))