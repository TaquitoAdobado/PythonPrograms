import speech_recognition as sr # Online
import pocketsphinx             # Offline 
"""
speech_recognition y pocketsphinx son dos librerias de Python que permiten el reconocimiento de voz.
No sé cuál estaré usando en la version final, por ahora estoy probando ambas. La opción online depende de la velocidad
de mi internet, si estoy en una red lenta, funciona mal
Sin embargo, la opción offline solo reconoce idioma inglés.
"""
import pyttsx3   #Para convertir texto a voz
#import pywhatkit  #Para darle acceso a YouTube, Google, etc.
#import pyjokes    #Para contar chistes

#import webbrowser #Para abrir paginas web
import datetime   #Para obtener la fecha y hora actual
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
        

def texto_a_voz(texto):
    ''' Esta funcion convertirá un mensaje de texto a voz. Interpretando al asistente de voz. '''

    # Inicializar el engine de texto a voz
    engine = pyttsx3.init()

    # Configuracion de la voz (opcional)
    engine.setProperty('rate', 140)  # Velocidad de la voz, 150 = velocidad normal
    engine.setProperty('volume', 1)  # Volumen de la voz (0.0 a 1.0)

    # Reproducir el texto
    engine.say(texto)
    engine.runAndWait()  # Esperar a que termine de hablar


def pedir_dia():
    ''' Esta funcion dira el dia de la semana actual. '''
    
    # Obtener el dia de la semana actual
    fecha  = datetime.date.today() # Obtener la fecha actual, 2025-06-06 por ejemplo

    dia_semana = fecha.weekday() # Obtener el dia de la semana, 0 = lunes, 6 = domingo

    dias_semana = {
        0: "Lunes",
        1: "Martes",
        2: "Miércoles",
        3: "Jueves",
        4: "Viernes",
        5: "Sábado",
        6: "Domingo"
    }
    
    # Informar al usuario el dia de la semana actual
    texto_a_voz(f"o, Hoy es {dias_semana[dia_semana]}") # Decir el dia de la semana actual

def pedir_hora():
    ''' esta funcion dira la hora actual. '''
    
    # Obtener la fecha con hora actual
    hora_actual = datetime.datetime.now() # 2025-06-06 12:00:00 por ejemplo

    # Obtener los datos necesarios, hora y minutos.
    hora = hora_actual.hour
    minutos = hora_actual.minute

    # Informar al usuario la hora actual
    texto_a_voz(f"a, Ahora son las {hora} horas con {minutos} minutos")