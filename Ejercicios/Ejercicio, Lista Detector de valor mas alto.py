#Cree una lista, usando el operador in , imprime el valor mas alto de la lista

My_list = [4, 6, 2, 15, 10, 13, 5]
valor_alto = My_list[0] #Indicamos que el valor mas alto es el de la posición 0 (aunque no sea cierto)

for i in My_list:       #Para cada posicion en la lista
    if i > valor_alto:  #Comparamos si cada posicion > valor_alto
        valor_alto = i  #Si cumple, sustituimos valor_alto
print (valor_alto)      #Resultado deberia ser 15

#En este ejercicio, la primer comparacion es de valor_alto con la posición 0
#por lo que se estará comparando el primer elemento con si mismo de forma innecesaria.