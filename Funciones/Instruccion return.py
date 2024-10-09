#Instrucción return SIN expresión, hara que la funcion finalice inmediatamente.

def happy_new_year(wishes=True):
    print("three...two...one...")
    if not wishes:
        return      #Cuando wishes sea False, return se ejecuta
    print("happy new year!!!")

happy_new_year() #Si dejamos el argumento sin especificar, tomara el valor default (True), por tanto.
#Salida = three... two... one... \n happy new year!!!

happy_new_year(False)   #Su nuestro argumento es False, return se activa y finaliza nuestra funcion.
#Salida = three...two...one...
  
  #-------------------------------------------------------------------------------------------

  #Instrucción return CON una expresión, hara que la funcion finalice inmediatamente.
  #Ademas, evaluará el valor de la expresión y lo devolverá como resultado.

def boring_function():
    return 123   #El argumento de return es 123

x = boring_function()
print("La funcion ha devuelto su resultado, el cual es:", x)
#Salida = La funcion ha devuelto su resultado, el cual es: 123


