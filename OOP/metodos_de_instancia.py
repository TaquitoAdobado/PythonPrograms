'''Los metodos son funciones que pertenecen a una clase.
Los metodos son usados para realizar acciones dentro de la clase'''

'''Los metodos de instancia son metodos que afectan al self, es decir a cada una de als instancias de la clase
Los metodos de instancia pueden: 
    - acceder y modificar los atributos de un objeto
    - acceder a otros metodos de la clase
    - modificar el estado de la clase
'''

class Pajaro:

    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    '''Para crear un metodo siempre se llama al self'''
    #Acceder y modificar los atributos de un objeto:
    def pintar_negro(self):
        self.color = 'negro'
        print(f"El pajaro ahora es {self.color}")


    #Acceder a otros metodos de la clase
    def volar(self,metros):
        print(f"El pajaro voló {metros} metros")
        self.piar()


    '''Al imprimir con '.format' se debe poner el self haciendo referencia al objeto'''
    def piar(self):
        print("Pio Pio, mi color sigue siendo {}".format(self.color))


piolin = Pajaro('amarillo','canario')   #Creamoa a piolin amarillo
piolin.pintar_negro()   #Modificamos el atributo color de piolin a negro
piolin.volar(50)    #invocamos el metodo volar que accede al metodo piar

#Modificar el estado de la clase
piolin.alas = False #cambiamos el estado alas de True a False
print(piolin.alas)
