'''
**kwargs / Argumentos de palabra clave / Keyword Argumeents
Sirven para identificar el argumento por su nombre. kwargs los agrupa en un diccionario.
Al igual que args, la palabra kwargs no es mandatoria, mientras tenga ** puede usarse cualquier palabra.
'''

def tipo_kwargs(**kwargs):
    return type(kwargs)

print(tipo_kwargs(x=1, y="dos", z=3))#Salida= <class 'dict'>
#Al funcionar como diccionarios, los argumentos van en grupo con su key y value
#al invocar la funcion, el key va sin comillas aunque sea string.


def desempaquetando_kwargs(**kwargs):
    for key, value in kwargs.items():
         print(f"Producto: {key}. Marca: {value}")

'''Tambien se puede usar un diccionario como **kwargs'''

kwargs ={'leche':"Lala", "Tv":"Samsung", "Telefono":"Redmi"}
desempaquetando_kwargs(**kwargs)
'''Salida: 
Producto: leche. Marca: Lala
Producto: Tv. Marca: Samsung
Producto: Telefono. Marca: Redmi'''
