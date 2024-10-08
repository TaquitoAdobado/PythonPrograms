#Una funcion parametrizada es cuando a un argumento le asignamos un valor "predeterminado" al crear la funcion.

def nombre_completo(nombre, apellido="Default"):    #El argumento apellido será Default, de forma predeterminada
    print("Mi nombre completo es: ", nombre, apellido)

nombre_completo("Juan","Perez")     #Si declaramos el argumento parametrizado, ignorará su valor predeterminado
#Salida: Mi nombre completo es: Juan Perez

nombre_completo("Juan")     #Si no declaramos el argumento parametrizado, se usará su valor predeterminado
#Salida: Mi nombre completo es: Juan Default