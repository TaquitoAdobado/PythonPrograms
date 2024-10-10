#En este ejercicio, se debera hacer una funcion que me diga si cuantos dias tiene un mes especificando de que año.
#Como febrero puede tener 28 o 29 dias dependiendo de si el año es bisiesto, se tendra que detecter si el año es bisiesto.
#Si el usuario ingresa un año fuera del calendario gregoriano (año<1582), o un valor inexistente de mes, la funcion
    #devolverá None

def año_bisiesto(año):      #Se crea funcion detectora de año bisiesto
    if año % 4 !=0:
        return False
    elif año % 100 !=0:
        return True
    elif año % 400 !=0:
        return False
    else:
        return True
        
def dias_en_mes(año, mes):  #Se crea funcion detectora de dias en mes
    if año<1582 or mes<1 or mes>12: #Se colocan condicionales para None
        return None
    dias = [31,28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  #Se crea una lista ordenada con los dias del mes. (Febrero con 28)
    if mes == 2 and año_bisiesto(año):  #Si el mes es 2(febrero) y el año es bisiesto
        return 29   #Si se cumple condicion, la respeusta sera 29 dias
    return dias[mes-1]  #Si no, respuesta es la posicion -1 del mes elegido. 
#Recordemos que las listas empiezan por la posicion 0. Si elijo 2 (para febrero, necesito la posicion 2 -1 en mi lista dias)

#Lo que el usuario ve:
print("Este programa te dice cuantos dias tiene el mes que tu elijas en el año que tu escribas")
año=int(input("ingrese el año:",))  #Asignamos valor a argumento año
mes=int(input("ingrese el numero de mes (ejemplo:3):",))    #Asignamos valor a argumento mes
print("El mes", mes, "del año", año, "tiene:", dias_en_mes(año,mes), "dias")