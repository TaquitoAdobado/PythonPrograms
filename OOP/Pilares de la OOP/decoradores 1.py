''' Los decoradores son patrones de diseño usados para dar nueva funcionalidad a las funciones.
Funciones que modifican funciones.  '''


def mayuscula(texto):
    print(texto.upper())


''' Las funciones en Python son objetos, por lo que pueden ser asignadas a variables.   '''

mi_funcion = mayuscula("prueba")
#Output: PRUEBA


''' Las funciones también pueden usarse como argumentos en otras funciones   '''

#Creamos una nueva funcion y como argumento de esta usaremos la funcion 'mayuscula' cuando se invoque
def nueva_funcion(funcion):
    return funcion

nueva_funcion(mayuscula("Estoy usando la funcion mayuscula como argumento de nueva_funcion"))
#Output: ESTOY USANDO LA FUNCION MAYUSCULA COMO ARGUMENTO DE NUEVA_FUNCION


''' Tambien se pueden definir funciones dentro de otras funciones
 (para este caso usaremos la funcion 'mayuscula' nombrada diferente para que no entre en conflicto con la anterior)
'''

def conversion_letras(tipo):

    #Definimos funciones de mayuscula y minuscula dentro de la funcion 'conversion_letras'.
    def a_mayuscula(texto):
        print(texto.upper())

    def a_minuscula(texto):
        print(texto.lower())

    #Creamos una condicion para saber si el argumento 'tipo' es 'mayuscula' o 'minuscula'
    if tipo == "may":
        return a_mayuscula
    elif tipo == "min":
        return a_minuscula

#Guardamos en una variable la funcion padre 'conversion_letras' con el tipo de conversion requerido.
operacion = conversion_letras("may")

#Invocamos a la variable (con la funcion) y con el texto que queremos convertir
operacion("Estoy usando una conversion de mayusculas")