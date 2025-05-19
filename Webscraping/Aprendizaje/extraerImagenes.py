# Dado el url, imprimir todas las imagenes de los libros que aparecen con el siguiente formato:
# Indice (puede iniciar en 0) - Nombre del libro : URL de la imagen
# Descargar la imagen del libro Scott Pilgrim´s

import requests
import bs4

url =  'https://books.toscrape.com/catalogue/page-1.html' #Esta es la url que usaremos
base = 'https://books.toscrape.com/'    #Esta es la base de la url, se usará para concatenar la url de la imagen


codigo_crudo = requests.get(url) #Primero debemos hacer una busqueda del codigo fuente de la pagina

#Lo convertimos en un formato que nos permita buscar lo requerido
codigo_bueno = bs4.BeautifulSoup(codigo_crudo.text, "lxml")

imagenes = codigo_bueno.select("img")   #Las imagenes que necesitamos se encuentran en la etiqueta img

#Creamos un bucle para recorrer la lista de imagenes e imprimir el indice, el nombre y la url
#El indice lo usaremos para identificar la imagen, este es el indice de la lista 'imagenes'
for imagen in imagenes:
    print(f" {imagenes.index(imagen)} - {imagen['alt']} : {base + imagen['src']}")
    # A cada imagen debemos agregarle la base del url y la url de la imagen para obtener la url completa

#Al tener nuestra lista, ya tenemos identificada la imagen que queremos descargar (indice 13).
url_imagen_seleccionada = base + imagenes[13]['src']
imagen_seleccionada = requests.get(url_imagen_seleccionada)

#Creamos el archivo donde guardaremos la imagen
archivo = open('Scott_Pilgrim.jpg', 'wb') #wb significa write binary (Las imagenes se guardan en binario).
archivo.write(imagen_seleccionada.content) #Escribimos el contenido de la imagen en el archivo
archivo.close() #Cerramos el archivo


