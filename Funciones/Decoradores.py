# Los decoradores son funciones que se encargan de modificar el comportamiento de otras funciones.
# Le da nuevas funcionalidades a otras funciones.

""" Un decorador se conforma de 3 funciones A, B y C, donde:
A recibe como parametro a B para devolver a C.


def funcion_decorador(funcion_B)
    def funcion_interna_C():
        #codigo que añade funcionalidades a la funcion B
        funcion_B()
    return funcion_interna_C

A es la funcion decoradora
B es la funcion a decorar
C es la funcion interna que da funcionalidades
"""

# Supongamos que tenemos una funcion que imprime una suma de 2 numeros.
"""
def suma(num1, num2):
    print(num1 + num2)
"""

# Pero ahora queremos que esa funcion imprima un saludo y una despedida.
# Entonces creamos la funcion decoradora (A) la cual le dara nombre al decorador. Su parametro hara referencia a la funcion a decorar (suma()).
def mensajes(funcion_suma):
    #Luego declaramos la funcion interna (C) que da funcionalidades a la funcion a decorar (B).
    #Como la funcion B puede o no recibir argumentos, colocamos *args y **kwargs para que pueda recibir cualquier tipo y cantidad.
    def funcion_interna_mensajes(*args, **kwargs):
        print("Hola, bienvenido")
        funcion_suma(*args, **kwargs)  #Llamamos a la funcion que queremos decorar. De esta forma el print tendra el saludo antes y la despedida despues de la suma.
        print("Adios")
    # Y ahora devolvemos la funcion interna (C). La indentacion del return corresponde a la funcion A
    return funcion_interna_mensajes

# Para finalizar, si queremos colocar un decorador a una funcion, debe hacerse usando la siguiente sintaxis AL MOMENTO de declarar la funcion:
''' 
@funcion_decoradora_A
def funcion_decorada_B():
    #Cuerpo de la funcion


Entonces pasamos de esto:

def suma(num1, num2):
    print(num1 + num2)

a esto:
'''
@mensajes
def suma(num1, num2):
    print(num1 + num2)

# Ahora al llamar a la funcion, se llamara con todo y el decorador.
suma(1, 2)

#Output:
'''
Hola, bienvenido
3
Adios
'''