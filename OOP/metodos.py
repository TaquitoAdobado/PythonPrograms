#Los metodos son funciones que pertenecen a una clase.
#Los metodos son usados para realizar acciones dentro de la clase

class Pajaro:
    def __init__(self, color):
        self.color = color

#Un metodo se crea igual que una funcion, pero siempre con el primer parametro self que hace referencia al objeto
    def volar(self,metros):
        print(f"El pajaro voló {metros} metros")

#Al imprimir con '.format' se debe poner el self haciendo referencia al objeto
    def piar(self):
        print("Pio, mi color es {}".format(self.color))

cuervo = Pajaro('Negro')
cuervo.volar(10)
cuervo.piar()
