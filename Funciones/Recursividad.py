#Recursividad: Tecnica donde una funcion se invoca a si misma
#Debe considerarse una condicion que detenga las invocaciones recursivas o el programa entra en un bucle infinito.

def fun(a):     #Se crea la función
    if a >31:   #Se crea condicion para detener las invocaciones recursivas
        return 3
    else:
        return a + fun(a+3)     #Se invoca la función dentro de la funcion (recursividad)
    
print(fun(25))
#Salida: 25 + 25+3 + 28+3 + 31+3 + 3
#La ultima suma es 3 ya que a=31+3=34, por lo que 34>31 y la condicion se cumple. Por ende el bucle termina.
#Salida = 87
