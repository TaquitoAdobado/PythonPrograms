''' 4to pilar de la OOP: Acoplamiento.
Mide la dependencia entre 2 modulos  distintos.
existe el acoplamiento fuerte y el acoplamiento debil.
Acoplamiento debil: No hay dependencia entre modulos. Situacion ideal.
Acoplamiento fuerte: Dependencia entre modulos. Situacion poco ideal.   '''

#Ejemplo de acoplamiento fuerte:
''' En el siguiente ejemplo, la clase Perro basa el comportamiento del metodo correr() en el atributo tiene_patas
de la clase Mascota. Teniendo un acoplamiento Fuerte ya que hay una dependecia entre la funcion de una clase y el 
atributo de otra.   '''
class Mascota:
    tiene_patas = True

class Perro:
    def correr(self, velocidad):
        if Mascota.tiene_patas:
            self.velocidad = velocidad

mi_mascota = Perro()
mi_mascota.correr("rapido")
print(mi_mascota.velocidad)