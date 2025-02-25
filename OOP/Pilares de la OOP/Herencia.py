''' La OOP tiene 6 pilares:
1. Herencia
2. Polimorfismo
3. Cohesion
4. Abstraccion
5. Acomplamiento
6. Encapsulamiento '''

#En este script se hablará sobre la Herencia
#Herencia es la capacidad de una clase Padre para heredar atributos y comportamientos a otra clase Hija.

#Se crea la clase padre, esta heredará los atributos y comportamientos a otras clases hijas.
class Animal:
    def __init__(self, color, edad):
        self.color = color
        self.edad = edad

    def nacer(self):
        print("He nacido!!!")

#Se crea la clase hija, esta heredara los atributos y comportamientos de la clase padre señalada entre parentesis.
class Gato(Animal):
    pass

#El objeto tom de la clase Gato comparte los atributos y comportamientos de la clase padre Animal
tom = Gato('Azul', 5)
tom.nacer()
print("Tom es un gato de color", tom.color, "y tiene", tom.edad, "años")

'''----------------Herencia extendida----------------'''
#La herencia extendida permite heredar atributos a niveles inferiores en la jerarquia de la clase.
print("\nHerencia extendida y multiple")
class Papa:
    def __init__(self, color_ojos, color_pelo):
        self.color_ojos = color_ojos
        self.color_pelo = color_pelo

    def saludar(self):
        print("Hola, mucho gusto")

class Mama:
    def saludar(self):  #Se crea un nuevo atributo con el mismo nombre de la clase padre
        print("Hello, how are you")

class Hijo(Papa, Mama):
    pass

class Nieto(Hijo):
    pass

nieto = Nieto('verde', 'marron')
print("Soy el nieto, Gracias a la herencia extendida, tengo los atributos de mi padre y abuelo")
nieto.saludar()
print("Heredé el saludo de mi Padre y no el de mi madre, porque asi fue el orden de herencia de mi Papá")

