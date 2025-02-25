''' 3er pilar de la OOP: Cohesion
La cohesion se refiere al grado de relacion entre los elementos de un modulo.
Cuando diseñmos una funcion, debemos identificar de un modo especifico que tarea realizará reduciendo
su finalidad a un objetivo unico y bien definido.
'''

#Cohesion debil: relacion entre elementos baja y no tiene una unica funcionalidad
''' En el siguiente ejemplo ademas de sumar 2 numeros, la funcion pide que se ingresen los numeros, en lugar de hacerlo
en otra funcion y pasarlos como argumentos. Asi mismo se hace la conversion a float dentro de la misma funcion.'''

def suma():
    num1 = float(int("inserte un numero"))
    num2 = float(int("inserte otro numero"))
    resultado = num1 + num2
    return resultado

#Cohesion fuerte: relacion entre elementos alta y tiene una unica funcionalidad
''' Para que la cohesion sea fuerte en el ejemplo anterior, seria conveniente que suma() realizara una unica tarea
bien definida, que es sumar. '''

def suma_numeros(lista_numeros):
    resultado = 0
    for num in lista_numeros:
        resultado += num
    return resultado

''' Ventajas de hacer codigo con cohesion fuerte:
1.- Reduce complejidad
2.- Mejora la legibilidad
3.- Reusabilidad de codigo '''
