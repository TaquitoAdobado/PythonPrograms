'''Para limpiar la consola importamos de os el metodo 'system'. Luego usamos el comando
'cls' o 'clear' dependiendo de nuestro sistema operativo'''
import os
from os import system

system("cls" if os.name=="nt" else "clear")
#"nt" es windows, con esta linea de codigo aseguramos que funcione tanto en windows como en Linux/MAC
#Podemos crear una funcion con esa linea de codigo para llamarla facilmente cuando queramos.
def limpiar_consola():
    system("cls" if os.name=="nt" else "clear")

nombre = input("Ingresa tu nombre: ")
edad = input("Ingresa tu edad: ")
limpiar_consola()

print(f"tu nombre es {nombre} y tienes {edad} años")