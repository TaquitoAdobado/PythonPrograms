#Los metodos estaticos son metodos que afectan a la clase, no a cada una de las instancias de la clase.
#Estos se declaran con el decorador @staticmethod

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

#creando un metodo estatico.
    @staticmethod
    def mirar():    #Como no se refiere ni a la clase ni la instancia, no lleva ni self ni cls
        print("Mirando")
        #No puede acceder a los atributos de la clase ni de las instancias
        #cls.alas = False // dara error
        #self.color = 'negro' // dara error

Pajaro.mirar()