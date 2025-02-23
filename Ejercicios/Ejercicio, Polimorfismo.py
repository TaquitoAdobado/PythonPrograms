'''
Crea 3 clases de personajes (Mago, Arquero, Espadachin), cada uno con un metodo de ataque diferente (basta con un
print de su ataque), posteriormente cree una instancia para cada clase y despues un iterador que logre un ataque
conjugado en el siguiente orden: Arquero, Mago, Espadachín.

Cree un metodo de defensa diferente para cada clase y posteriormente declare una funcion llamada defensa() que pueda
recibir una instancia y ejecutar su metodo de defensa, independientemente de que personaje sea.
'''

class Mago():
    def atacar(self):
        print("¡Fire storm!")

    def defender(self):
        print('Escudo magico')

class Arquero():
    def atacar(self):
        print("¡Critical arrow!")

    def defender(self):
        print("Bloqueo con arco")

class Espadachin():
    def atacar(self):
        print("¡Sacred sword!")

    def defender(self):
        print("Bloqueo con escudo")

gandalf = Mago()
legolas = Arquero()
aragon = Espadachin()

personajes = [legolas, gandalf, aragon]
print('ataque conjugado!:')
for per in personajes:
    per.atacar()

def defensa(personaje):
    return personaje.defender()

print("\ndefensas:")
defensa(gandalf)
defensa(legolas)
defensa(aragon)