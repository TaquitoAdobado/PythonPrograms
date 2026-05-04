# Wrap es una funcion que se usa para copiar los metadatos de una funcion original a una funcion envoltura
# Por ejemplo, supongamos que tenemos la siguiente funcion decorada:

def decoradora(funcion):
    def funcion_envoltura(*args, **kwargs):
        """Esta es la funcion envoltura, que agrega saludo y despedida"""
        print("hola, sumemos 2 numeros")
        funcion(*args, **kwargs)
        print("Adios")

    return funcion_envoltura

@decoradora
def suma(num1, num2):
    """Esta funcion hace la suma de 2 numeros"""
    print(num1 + num2)

#Si nosotros ahora imprimimos los metadatos de nombre y docstring de la funcion suma que esta decorada y envuelta por la funcion_envoltura:
print(suma.__name__)    # Output: funcion_envoltura 
print(suma.__doc__)     # Output: Esta es la funcion envoltura, que agrega saludo y despedida

#Podemos ver que se imprimen los datos de la funcion envoltura, y no los de la funcion original.

#Para solucionar esto, podemos usar la funcion wraps de la libreria functools

from functools import wraps

# Ahora decoremos una funcion que resta 2 numeros, dandole un saludo y una despedida.
# Pero coloquemos el decorador @wraps antes de la funcion_envoltura

def nuevo_decorador(funcion):
    @wraps(funcion)
    def funcion_envoltura(*args, **kwargs):
        """Esta es la funcion envoltura, que agrega saludo y despedida"""
        print("hola, restemos 2 numeros")
        funcion(*args, **kwargs)
        print("Adios")

    return funcion_envoltura

# Declaremos la funcion resta con el nuevo decorador
@nuevo_decorador
def resta(num1, num2):
    """Esta funcion hace la resta de 2 numeros"""
    print(num1 - num2)

# Ahora imprimamos sus metadatos de nombre y docstring para ver que pasa.

print(resta.__name__)    # Output: resta
print(resta.__doc__)     # Output: Esta funcion hace la resta de 2 numeros

# Como podemos ver en el output, gracias al wraps, se imprimen los metadatos de la funcion original y no de la funcion envoltura.
