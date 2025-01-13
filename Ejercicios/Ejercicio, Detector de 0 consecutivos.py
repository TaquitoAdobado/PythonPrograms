def detector_cero_consecutivo(*args):
    '''Esta funcion deberá poder recibir una cantidad indefinida de numeros y devolverá
    True si contiene el numero 0 repetido 2 veces consecutivas, de lo contrario devolverá
    False'''
    lista=list(args)
    primer_valor=lista[0]

    for numero in lista[1:]:
        if numero==0 and primer_valor==0:
            return True
        else:
            primer_valor=numero
            pass
    return False
print(detector_cero_consecutivo(0,1,0,1,0,3,8,0))