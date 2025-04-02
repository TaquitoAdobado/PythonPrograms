''' Continuando con los decoradores. Usaremos un decorador para adornar una funcion agregandole
un saludo y una despedida.  '''

def decorar_saludo(funcion):

    def funcion_interna(palabra):
        print("Bienvenido")
        funcion(palabra)
        print("Hasta pronto\n")

    return funcion_interna

''' Ahora crearemos una funcion que usaremos como argumento de decorar_saludo. 
podemos usar @decorar_saludo antes de declarar la funcion que queremos decorar  '''

@decorar_saludo
def mayuscula(texto):
    print(texto.upper())

''' invocamos a la funcion que ya fue decorada con el saludo y la despedida '''

mayuscula("este texto tiene un saludo y una despedida")
#OUTPUT:
'''     Bienvenido
        ESTE TEXTO TIENE UN SALUDO Y UNA DESPEDIDA
        Hasta pronto                                '''

'''Si se desea tener la opcion de no decorar la funcion, definimos la funcion con opcion a decorar, posteriormente
se agrega la funcion decoradora a una variable y se agrega como argumento la funcion que se quiera decorar
(en caso de querer) '''

def minuscula(texto):
    print(texto.lower())

decorador = decorar_saludo(minuscula)

''' Invocamos a la funcion con la decoracion'''
decorador("ESTE TEXTO ESTARÁ EN MINUSCULA Y DECORADO CON UN SALUDO Y UNA DESPEDIDA")
#Output:
'''     Bienvenido
        este texto estará en minuscula y decorado con un saludo y una despedida
        Hasta pronto                                '''


''' Si no se quiere usar el decorador simplemente se invoca a la funcion sin el decorador '''
minuscula("ESTE TEXTO ESTARÁ EN MINUSCULA Y NO ESTARÁ DECORADO CON SALUDO NI DESPEDIDA")
#Output:
''' este texto estará en minuscula y no estará decorado con saludo ni despedida '''
