'''Los metodos de clase son metodos que afectan a la clase, no a cada una de las instancias de la clase.
Estos se declaran con el decorador @classmethod y se definen con la palabra reservada "cls" en lugar de "self"  '''

class Pajaro:
    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print("Pio")

    def volar(self,metros):
        print(f"El pajaro volí {metros} metros")
        self.piar()

    def pintar_negro(self):
        self.color = 'negro'

    @classmethod
    def poner_huevos(cls, cantidad):
        print(f"Puso {cantidad} huevos")
        # Al ser un metodo de clase no puede acceder a los atributos de instancia
        # print(f"Es de color {self.color} y de especie {self.especie}") dara error

# El metodo de clase no necesita una instancia para poder ejecutarse
Pajaro.poner_huevos(3)

#Los metodos de clase igual que los de instancia, pueden acceder y modificar los atributos de la clase
Pajaro.alas = False    #Cambiamos el estado alas de True a False
print(Pajaro.alas)