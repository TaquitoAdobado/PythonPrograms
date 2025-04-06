import os
from os import system

#-----------------------Funciones auxiliares-----------------------
def limpiar_pantalla():
    system("cls" if os.name == "nt" else "clear")


#-----------------------Funciones Generadores-----------------------
def farmacia():
    for turno in range(1, 10000):
        yield f" F - {turno}"


def perfumeria():
    for turno in range(1, 10000):
        yield f" P - {turno}"


def cosmeticos():
    for turno in range(1, 10000):
        yield f" C - {turno}"

#-----------------------Funciones Decoradoras-----------------------
def decorador_turno(seccion_tienda):
    print("\n" + "*" * 23)
    print(f"Su turno es: ")
    try:
        if seccion_tienda == seccion_farmacia:
            print(next(generador_farmacia))
        elif seccion_tienda == seccion_perfumeria:
            print(next(generador_perfumeria))
        elif seccion_tienda == seccion_cosmeticos:
            print(next(generador_cosmeticos))
        else:   #Numero no existente.
            print("Ops, esa tienda no existe, intenta nuevamente.")
    except StopIteration:   #Si el generador se agota, se lanza un error.
        print("\n ***** ERROR ***** \nTurnos agotados. \nLamentamos las molestias.")
    print("\nDisfrute su visita.")
    print("*" * 23 + "\n")


#-----------------------Funciones Estructura-----------------------
def menu_principal():
    print("*" * 23)
    print("BIENVENIDO. \n\n¿A que area desea ingresar?")
    print("\n1.- Farmacia \n2.- Perfumeria \n3.- Cosmeticos")
    print("*" * 23 + "\n")


def seleccion_area():
    #Se utiliza try/except para manejar errores en caso de que se ingrese un valor no entero.
    try:
        seleccion_tienda = int(input("(Seleccione el numero del area): "))
        limpiar_pantalla()
        return seleccion_tienda #Se retorna el numero ingresado(1-3) para llamar a la función decoradora más adelante.
                                #Si se ingresó un numero distinto, se manejará un error al llamar al generador.
    except ValueError:  #Si se ingresa un valor no entero se manejará un error al llamar al generador.
        limpiar_pantalla()
        pass

#Esta función preguntará al usuario si desea tomar otro turno, al decir que no, finalizará el programa.
#Esta función no es tan necesaria, pero me pareció interesante agregarla.
def salir():
    while True:
        otro_turno = input("¿Desea tomar otro turno? (s/n): ").lower()
        if otro_turno == "s":
            limpiar_pantalla()
            return otro_turno
        elif otro_turno == "n":
            limpiar_pantalla()
            return otro_turno
        else:
            limpiar_pantalla()
            print("Respuesta no valida, intenta nuevamente.")

#Funcion principal del programa, se ejecuta hasta que el usuario decida salir después de tomar algún turno.
def main():
    while True:
        menu_principal()
        decorador_turno(seleccion_area())
        continuar = salir()
        if continuar == "s":
            continue
        else:
            break
    print("\nGracias por usar el programa")


#-----------------------Ejecución del programa-----------------------
#Constantes globales, usadas para llamar a las funciones decoradoras
seccion_farmacia = 1
seccion_perfumeria = 2
seccion_cosmeticos = 3
#Se crean los generadores para cada tienda
generador_farmacia = farmacia()
generador_perfumeria = perfumeria()
generador_cosmeticos = cosmeticos()
#Se ejecuta el programa
main()