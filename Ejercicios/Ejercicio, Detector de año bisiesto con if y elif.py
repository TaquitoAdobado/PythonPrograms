#CALENDARIO GREGORIANO A PARTIR DEL AÑO 1582
#DETERMINAR SI EL AÑO INGRESADO ES BISIESTO O COMUN
#si el número del año no es divisible entre cuatro, es un año común.
#de lo contrario, si el número del año no es divisible entre 100, es un año bisiesto.
#de lo contrario, si el número del año no es divisible entre 400, es un año común.
#de lo contrario, es un año bisiesto.
#utiliza los operadores != y %

año = int(input("ingrese un año para determinar si es bisiesto o comun: "))

if año < 1582:
    print("el año no es del calendario Gregoriano (debe ser a partir del 1582)")
else:
    if año%4 != 0:
        print("El año: ", año, " es COMUN.")
    elif año%100 !=0:
        print("El año: ", año, " es BISIESTO.")
    elif año%400 !=0:
        print("El año: ", año, " es COMUN")
    else:
        print("El año: ", año, " es BISIESTO")


# 2000 - Bisiesto
# 2015 - Comun
# 1999 - Comun
# 1996 - Bisiesto
# 1580 - no es parte del calendario Gregoriano
