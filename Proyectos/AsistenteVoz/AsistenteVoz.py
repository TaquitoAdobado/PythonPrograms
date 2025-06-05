"""
speech_recognition y pocketsphinx son dos librerias de Python que permiten el reconocimiento de voz.
No sé cuál estaré usando en la version final, por ahora estoy probando ambas. La opción online depende de la velocidad
de mi internet, si estoy en una red lenta, funciona mal
Sin embargo, la opción offline solo reconoce idioma inglés.
"""

import speech_recognition as sr # Online
import pocketsphinx             # Offline 

#import pyttsx3N   #Para convertir texto a voz
#import pywhatkit  #Para darle acceso a YouTube, Google, etc.
#import pyjokes    #Para contar chistes

#import webbrowser #Para abrir paginas web
#import datetime   #Para obtener la fecha y hora actual
#import wikipedia  #Para buscar en Wikipedia
import time        #Para medir tiempos

#Escuchar nuestro microfono y devolver el audio como texto

def audio_a_texto_online():

    #Almacenar el reconocimiento de voz en una variable
    recognizer = sr.Recognizer()

    #Configuramos el microfono
    with sr.Microphone() as source: #Microfono por defecto como fuente

        #Tiempo de espera para empezar a escuchar
        recognizer.pause_threshold = 1 #Segundos

        #Informar que inicio la grabacion
        print( "\nEmpieza a hablar, tienes 5 segundos:\n")

        #Guardar lo que diga el usuario
        user_audio = recognizer.listen(source, phrase_time_limit= 5) #Limitar el tiempo de grabacion a 5 segundos   

        #try/except para manejar posibles errores de entendimiento
        try:
            #Buscar en google lo que nos diga el usuario
            user_request = recognizer.recognize_google(user_audio, language = "es-mx") #Sphinx solo reconoce ingles.
            
            #Prueba de que se haya entendido
            print(f"Tu peticion es: \n{user_request}")

            #Devolver la peticion
            return user_request

        #En caso de no comprender el audio
        except sr.UnknownValueError:

            #Prueba de que no se comprendio el audio
            print("Oops, no entendi tu peticion")

            #Devolver error
            return "Sigue intentando"

        #En caso de haber grabado el audio pero no poder transformarlo a string
        except sr.RequestError:
            # Mensaje de prueba
            print("Oops, tuve un error al procesar tu peticion")

            # Devolver error
            return "Sigue intentando"

        #Errores inesperados o no contemplados
        except:
            # Mensaje de prueba
            print("Oops, algo salió mal")

            # Devolver error
            return "Sigue intentando"
        


print("\nVoz a Texto - ONLINE")
inicio_online = time.time() #Iniciar el temporizador
audio_a_texto_online()
fin_online = time.time() #Finalizar el temporizador
print(f"\nTiempo de ejecución: {fin_online - inicio_online} segundos")


