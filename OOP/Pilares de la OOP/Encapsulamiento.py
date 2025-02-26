''' 6to pilar de la OOP: Encapsulamiento.
Se relaciona con ocultar al exterior determinados estados internos de un objeto tal que sea el mismo
objeto quien acceda o los modifique, pero dicha accicon no se pueda llevar a cabo desde el exterior llamando a
los metodos o atributos directamente.
'''

#En Python esto se hace anteponiento 2 guiones bajos (__) al nombrar un metodo o un atributo para definirlos como
#   privados, donde únicamente el mismo objeto podrá acceder a ellos.

class Persona:
    atributo_publico = "Mostrar"    #Accesible desde el exterior
    __atributo_privado = "Oculto"   #No accesible

    #No accesible desde el exterior
    def __metodo_oculto(self):
        print("Este metodo está oculto")
        self.__variable = 0
        print(self.__variable)
    #Accesible desde el exterior:
    def metodo_normal(self):
        #El metodo si es accesible desde el interior
        self.__metodo_oculto()

alumno = Persona()
#alumno.__metodo_oculto()   #Este metodo no es accesible desde el exterior
alumno.metodo_normal()  #Este metodo es accesible
