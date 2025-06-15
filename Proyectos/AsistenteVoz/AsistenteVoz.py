import speech_recognition as sr # Online
import pocketsphinx             # Offline 
"""
speech_recognition y pocketsphinx son dos librerias de Python que permiten el reconocimiento de voz.
No sé cuál estaré usando en la version final, por ahora estoy probando ambas. La opción online depende de la velocidad
de mi internet, si estoy en una red lenta, funciona mal
Sin embargo, la opción offline solo reconoce idioma inglés.
"""
import pyttsx3              #Para convertir texto a voz
import pywhatkit            #Para darle acceso a YouTube, Google, enviar mensajes por WA, etc.
import pyjokes              #Para contar chistes

#import webbrowser          #Para abrir paginas web
import datetime             #Para obtener la fecha y hora actual
#import wikipedia           #Para buscar en Wikipedia
import time                 #Para medir tiempos
from random import choice   #Para elegir un elemento aleatorio de una lista

#Escuchar nuestro microfono y devolver el audio como texto

def audio_a_texto_online():

    #Almacenar el reconocimiento de voz en una variable
    recognizer = sr.Recognizer()

    #Configuramos el microfono
    with sr.Microphone() as source: #Microfono por defecto como fuente
        
        #Tiempo de espera para empezar a escuchar
        recognizer.pause_threshold = .5 #Segundos

        #Informar que inicio la grabacion
        print( "\nEmpieza a hablar, tienes 10 segundos:\n")

        #Guardar lo que diga el usuario
        user_audio = recognizer.listen(source, phrase_time_limit= 10) #Limitar el tiempo de grabacion a 10 segundos   
        
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
            mensaje = "Silencio o no se comprendio el audio"
            print(mensaje)
            return mensaje

        #En caso de tener problemas de conexion a internet
        except sr.RequestError:
            mensaje = "No se pudo conectar al servicio de reconocimiento de voz"
            print(mensaje)
            return mensaje

        #Errores inesperados o no contemplados
        except:
            mensaje = "Error desconocido, intenta de nuevo"
            print(mensaje)
            return mensaje
        

def texto_a_voz(texto):
    ''' Esta funcion convertirá un mensaje de texto a voz. Interpretando al asistente de voz. '''

    # Inicializar el engine de texto a voz
    engine = pyttsx3.init()

    # Configuracion de la voz (opcional)
    engine.setProperty('rate', 150)  # Velocidad de la voz, 150 = velocidad normal
    engine.setProperty('volume', 1)  # Volumen de la voz (0.0 a 1.0)

    # Reproducir el texto
    engine.say(texto)
    engine.runAndWait()  # Esperar a que termine de hablar


def pedir_dia():
    ''' Esta funcion dira el dia de la semana actual. '''
    
    # Obtener el dia de la semana actual
    fecha  = datetime.date.today() # Obtener la fecha actual, 2025-06-06 por ejemplo

    dia_semana = fecha.weekday() # Obtener el dia de la semana, 0 = lunes, 6 = domingo
    dia_actual = fecha.day # Obtener el dia actual, 12 por ejemplo
    mes_actual = fecha.month # Obtener el mes actual, 6 = junio por ejemplo
    año_actual = fecha.year # Obtener el año actual, 2025 por ejemplo
    dias_semana = {
        0: "Lunes",
        1: "Martes",
        2: "Miércoles",
        3: "Jueves",
        4: "Viernes",
        5: "Sábado",
        6: "Domingo"
    }

    nombre_mes = {
        1: "Enero",
        2: "Febrero",
        3: "Marzo",
        4: "Abril",
        5: "Mayo",
        6: "Junio",
        7: "Julio",
        8: "Agosto",
        9: "Septiembre",
        10: "Octubre",
        11: "Noviembre",
        12: "Diciembre"
    }
    
    # Informar al usuario el dia de la semana actual
    texto_a_voz(f"hmm, Hoy es {dias_semana[dia_semana]} {dia_actual} de {nombre_mes[mes_actual]} del {año_actual}") # Decir el dia de la semana actual


def pedir_hora():
    ''' esta funcion dira la hora actual. '''
    
    # Obtener la fecha con hora actual
    hora_actual = datetime.datetime.now() # 2025-06-06 12:00:00 por ejemplo

    # Obtener los datos necesarios, hora y minutos.
    hora = hora_actual.hour
    minutos = hora_actual.minute

    # Informar al usuario la hora actual
    texto_a_voz(f"hmm, Ahora son las {hora} horas con {minutos} minutos")


def saludo_inicial():
    ''' Esta funcion saluda de manera difetente al usuario dependiendo de la hora del dia. '''

    # Obtener la hora actual
    hora_actual = datetime.datetime.now()  # 2025-06-06 12:00:00 por ejemplo
    hora = hora_actual.hour  # Obtener la hora actual, 12 por ejemplo

    # Determinar el saludo dependiendo de la hora

    # Saludo por la mañana
    if 6 <= hora < 12:
        texto_a_voz("hmm, ¡Buenos dias!, mi nombre es elena, si necesitas algo menciona mi nombre.")

    # Saludo por la tarde
    elif 12 <= hora < 20:
        texto_a_voz("hmm, ¡Buenas tardes!, mi nombre es elena, si necesitas algo menciona mi nombre.")
    
    # Saludo por la noche
    else:
        texto_a_voz("hmm, ¡Buenas noches!, mi nombre es elena, si necesitas algo menciona mi nombre.")


def pedir_chiste():
    ''' Esta funcion pide un chiste al usuario. '''
   
    # Obtener un chiste aleatorio
    chiste = pyjokes.get_joke(language= 'es', category= 'all')  # Obtener un chiste en español
    
    # Contar el chiste al usuario
    texto_a_voz(chiste)


def buscar_en_internet():
    ''' Esta funcion permite buscar en internet lo que el usuario pida. '''
    
    # Escuchar al usuario y convertir su peticion a minusculas
    pedido = audio_a_texto_online().lower()
    pedido = pedido.replace("busca en internet", "")  # Eliminar la frase "busca en internet" de la peticion
    pedido = pedido.replace("busca en google", "")  # Eliminar la frase "busca en google" de la peticion

    # Informar al usuario que se esta buscando
    texto_a_voz("hmmm, enseguida lo busco.")

    # Usar pywhatkit para buscar en Google (abre el navegador con el resultado)
    pywhatkit.search(pedido)
    # Informar al usuario que se ha completado la busqueda
    texto_a_voz(f"hmmm, abriendo resultado en navegador.")


def responder_insulto():
    ''' Esta funcion responde a los insultos del usuario. '''

    respuestas = [
    "hmmm, talvez sea eso, pero seré mas educada que tu. Que tengas bonito día.",
    "hmmm, almenos a mí si me enseñaron a no ser grosera. Disfruta tu día.",
    "hmmm, si así de sucia tienes la boquita, no me quiero ni imaginar tu... ejem. Hasta pronto.",
    "hmmm, está mal enojarse de esa manera, ¿qué dirían tus padres o abuelos si te escucharan?. Piénsalo.",
    "hmmm, yo no soy la persona que se está peleando con un asistente de voz, jajaja Nos vemos."
    ]
    # Elegir una respuesta aleatoria de la lista de respuestas
    respuesta = choice(respuestas)

    # Responder al usuario la respuesta
    texto_a_voz(respuesta)
    

def centro_de_control():
    ''' Esta funcion es el centro de control del asistente de voz. Depende de la peticion del usuario, será la accion a realizar. '''
    
    pedido = audio_a_texto_online().lower() # Escuchar al usuario y convertir su peticion a minusculas

    #Seleccion de peticiones

    # Si el usuario pide la hora
    if any(palabra in pedido for palabra in [
        "qué hora es",
        "dime la hora",
        "hora actual",
        "a qué hora estamos"
        ]):
        pedir_hora()
        return
    
    # Si el usuario pide el dia de la semana
    elif any(palabra in pedido for palabra in [
        "qué día es",
        "dime el día",
        "día de la semana",
        "qué día de la semana es",
        "qué día es hoy",
        ]):
        pedir_dia()
        return
    
    #Si el usuario saluda al asistente de voz
    elif any(palabra in pedido for palabra in [
        "salúdame",
        "hola"
    ]):
        texto_a_voz("hmm, Hola, espero que estés teniendo un dia precioso")
        return
    
    #Si el usuario pide un chiste
    elif any(palabra in pedido for palabra in [
        "cuentame un chiste",
        "dime un chiste",
        "quiero escuchar un chiste",
        "hazme reir",
        "cuenta un chiste"
    ]):
        pedir_chiste()
        return
    
    #Si el usuario pide que busque en internet
    elif "busca en internet" in pedido:
        buscar_en_internet()
        return
    
    #Si el usuario le dice una groseria al asistente.
    elif any(palabra in pedido for palabra in [
        "pendeja",
        "puta",
        "estupida",
        "maricona",
        "perra",
        "babosa",
        "imbesil" or "imbecil",
        "tonta"
    ]):
        responder_insulto()
        return
        
    else:
        #Si se pide algo que no se tenga contemplado
        texto_a_voz("Lo siento, no puedo ayudarte con eso. Por favor, intenta de nuevo.")
        return


#-------------------Programa principal--------------------

# Saludo inicial al usuario
saludo_inicial() 

# Bucle principal del asistente de voz
while True:
    llamada = audio_a_texto_online().lower() # Se escuchará al usuario hasta que diga "elena"
    if "elena" or "helena" in llamada:
        texto_a_voz("hmmm, ¿en qué puedo ayudarte?")
        centro_de_control() # Llamar al centro de control del asistente de voz
    else:
        continue # Si no se menciona el nombre del asistente, se vuelve a escuchar al usuario