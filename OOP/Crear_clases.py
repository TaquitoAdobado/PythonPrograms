'''
Una clase en Python es una plantilla o molde que se utiliza para crear objetos.
Proporciona la estructura para definir características (atributos)
y comportamientos (métodos) de los objetos.
'''

#Para crear una clase usamo 'class' + nombre de la clase con la primera letra en mayúscula:

class Animal:   #Se creó la clase Animal
    pass

perro = Animal() #Se creo un objeto de la clase Animal
print(type(perro))  #Salida: <class '__main__.Animal'>
'''
__main__ significa que la clase se encuentra en el mismo archivo
.Animal indica el objeto perro pertenece a la clase Animal
'''