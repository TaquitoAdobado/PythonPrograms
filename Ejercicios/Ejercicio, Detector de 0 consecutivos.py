def detector_cero_consecutivo(*args):
    '''Esta funcion deberá poder recibir una cantidad indefinida de numeros y devolverá
    True si contiene el numero 0 repetido 2 veces consecutivas, de lo contrario devolverá
    False'''
    primer_valor=args[0]

    for numero in args[1:]:
        if primer_valor==0 and numero==0:
            return True
        else:
            primer_valor=numero
            pass
    return False
print(detector_cero_consecutivo(5,6,1,0,0,9,3,5)) #True
print(detector_cero_consecutivo(6,0,5,1,0,3,0,1)) #False