'''Usados en casos donde no se conoce de antemano el numero exacto de argumentos que pasarán en una funcion.
Se usa la sintaxis *args para referirse a los argumentos adicionales.
El nombre *args no es mandatorio, sin embargo, es sugerido como buena practica.
Cualquier nombre iniciado en * referirá a esros argumentos de cantidad variable'''

def sumatoria_argumentos(*args):
    sumatoria=sum(args) #Para usarlo se llama sin el *
    print(sumatoria)

sumatoria_argumentos(1,2,3,4,5)# *args iterará por todos los argumentos indefinidos dados al invocar la funcion
    #Salida = 15

'''Los *args tambien pueden ser desempaquetados de una lista'''
args = [20,30,50]
sumatoria_argumentos(*args)#Al invocarse se hace uso del *
#Salida = 100