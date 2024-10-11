#Usando la Funcion de año bisiesto y la Funcion Dias en mes realizadas en ejercicios anteriores, se crea una funcion que indice
    #la cuenta de dias en una fecha especifica empezando desde enero 1. Recordando que en año bisiesto, febrero tiene un dia mas.

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

def dias_totales(año, mes, dia):    #Se crea funcion contadora de dias transcurridos dentro de una fecha especifica.
    dias_totales=0
    if dias_en_mes(año, mes)==None or dia<1 or dia>31 or mes==2 and dia>29: #Condiciones para None (fechas inexistentes)
        return None
    dias = [31,28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  #Se crea lista de dias por cada mes
    for i in range(mes-1):  
        dias_totales+= dias[i]  #por cada iteracion del for se van sumando los dias de la lista hasta mes -1. mas adelante se suma dia
    if año_bisiesto(año) and mes>2: #Si el año es bisiesto y mes>2
        dias_totales+=1 + dia       #dias_totales= suma de iteraciones + argumento dia. Como es bisiesto le sumamos el dia extra de febrero
        return dias_totales         #termina funcion devolviendo sumatoria anterior
    dias_totales+=dia   #Como no es bisiesto, dias_totales= suma de iteraciones + argumento dia.
    return dias_totales #Termina funcion delviendo sumatoria anterior.
    
print(dias_totales(2024, 12, 31))   #Se invoca funcion declarando(año, mes, dia)

#Nota de mejora: Se repitió lista dias[ ] en funcion 2 y 3, se pudo declarar fuera de las funciones y usarse como argumento.