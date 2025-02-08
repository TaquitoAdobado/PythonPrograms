'''
Crea una clase llamada Personaje, y asígnale el siguiente atributo de clase:
real = False
Crea una instancia llamada harry_potter con los siguientes atributos de instancia:
especie = "Humano"
magico = True
edad = 17

imprime lo siguiente:
Harry Potter es: Humano
Harry Potter es magico: True
Harry Potter tiene: 17 años
Harry Potter es real: False
'''

class Personaje:
    real = False
    def __init__(self, especie, magico, edad):
        self.especie = especie
        self.magico = magico
        self.edad = edad

harry_potter = Personaje('Humano', True, 17)
print('Harry Potter es:', harry_potter.especie)
print('Harry Potter es magico:', harry_potter.magico)
print('Harry Potter tiene:', harry_potter.edad, 'años')
print('Harry Potter es real:', harry_potter.real)