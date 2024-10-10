#Detector de contraseña con while e if

respuesta = False # La dejamos en False para usarlo en el while.
palabra_correcta = "ESPATIFILO" #Mi contraseña correcta será esta.

while respuesta == False: # Mientras respuesta sea False (al ingresar una contraseña incorrecta) repetirá el Loop.
    palabra = input("ingrese la contraseña, pista(espatifilo gritado):") #Aqui comienza el Loop pidiendo la contraseña
                    
    if palabra == "ESPATIFILO": #Si se ingresa contraseña correcta
        print ("contraseña correcta")
        respuesta = True # Respuesta pasa a ser True y el ciclo termina.
        exit() #Termina el programa
                    
    elif palabra == "espatifilo": #Si se ingresa contraseña correcta pero en minuscula
        print ("contraseña incorrecta, no la gritaste") #Avisar que esta mal porque no se gritó (pista para poner en mayuscula
        respuesta = False #Respuesta = False por lo que el bucle se repite desde ingresar contraseña
                    
    else:           #Si se ingresa contraseña erronea
        print("contraseña incorrecta")
        respuesta = False   # Repetir Loop desde ingresar contraseña
