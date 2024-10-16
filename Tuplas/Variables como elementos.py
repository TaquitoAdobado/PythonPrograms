#Los elementos en una tupla pueden ser variables

var1 = 2
var2 = "im var2"

tuple_var = (1, var1, var2)

print(tuple_var)    #Salida= (1, 2, 'im var2')


#No se pueden editar las variables en una tupla despues de ser creada

var1 = 20
var2 = "im the new var2?"

print(tuple_var)     #Salida= (1, 2, 'im var2')

#La tupla cambiaría si se vuelve a crear sobre la misma dirección, tecnicamente se sobreescribiría.

var1 = 20
var2 = "im the new var2!"
tuple_var = (1, var1, var2)
print(tuple_var)     #Salida= (1, 20, 'im the new var2!')