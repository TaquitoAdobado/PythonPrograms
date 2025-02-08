'''
Los atributos son variables que se definen dentro de una clase.
Existen 2 tipos de atributos: de instancia y de clase.
Los atributos de clase son compartidos por todos los objetos de la clase.
Los atributos de instancia son diferentes para cada objeto de la clase.
'''

#Atributos de instancia

class Pajaro:
    def __init__(self, color):  #Creamos el constructor de la clase Pajaro
        self.color = color #Creamos el atributo de clase

    #__init__ es el constructor de la clase
    #self es el objeto que se esta creando, es obligatorio, puede ser otro nombre (no recomendado)
    #color es el parametro que se pasa a la clase
    #self.color es el atributo de la clase

pajaro_1 = Pajaro('negro') #negro es el parametro que se pasa a la clase Pajaro
pajaro_2 = Pajaro('amarillo') #amarillo es el parametro que se pasa a la clase Pajaro

print('El color del pajaro 1 es: ', pajaro_1.color)
print('El color del pajaro 2 es: ', pajaro_2.color)
print('Como el atributo color es diferente para cada objeto Pajaro, es un atributo de instancia')

#Atributos de clase

class Perro:
    patas = 4 #Se crea un atributo de clase

labrador = Perro()
Pug = Perro()

print("\nLos perros Labrador tienen ",labrador.patas, "patas")
print("los Pug tambien tienen", Perro.patas, "patas")
print("Como todos los objetos Perro tienen el mismo atributo de 'patas', es un atributo de clase")


