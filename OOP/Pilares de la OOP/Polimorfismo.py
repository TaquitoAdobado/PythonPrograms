'''
2do pilar de la OOP: Polimorfismo.
El polimorfismo nos permite que diferentes objetos de clases distintas, puedan ejecutar un metodo con el mismo nombre,
pero con diferentes comportamientos.
'''

class Vaca:

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):   #Se crea el metodo hablar para la clase Vaca
        print(self.nombre, "muuu")

class Oveja:

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):   #Se crea el metodo hablar para la clase Oveja
        print(self.nombre, "beee")

#Se crean 2 objetos de las diferentes clases
vaca_1 = Vaca('Vaquencia')
oveja_1 = Oveja('Overto')

#Se usa el metodo con el mismo nombre en los objetos de las clases diferentes, cada uno con su propio comportamiento.
vaca_1.hablar()
oveja_1.hablar()

''' Tambien funciona sobre iteraciones'''

print("\nPolimorfismo sobre iteraciones en una lista")
animales = [vaca_1, oveja_1]
for obj in animales:
    obj.hablar()

''' Tambien funciona sobre funciones'''

def hablar(animal):
    return animal.hablar()

print("\nPolimorfismo en una funcion")
hablar(vaca_1)
hablar(oveja_1)