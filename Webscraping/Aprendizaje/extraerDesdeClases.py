#17/05/2025 la pagina contiene un cuadro de texto debajo del titulo con 2 enlaces nombrados:
# "CURSOS" y "YOUTUBE"
#Extraer los enlaces de ambos usando la clase que las contenga.
#Extraer los nombres de los enlaces
# https://escueladirecta-blog.blogspot.com/

import requests
import bs4

url = 'https://escueladirecta-blog.blogspot.com/'

#Almacenamos el codigo html en una variable
busqueda = requests.get(url)

#Lo convertimos en un formato que nos permita buscar lo requerido
sopa = bs4.BeautifulSoup(busqueda.text, "lxml")

#Buscamos la clase, para esto nos apoyamos de "inspeccionar elemento" usando click derecho (desde el navegador)
#en lo que queramos buscar.

#Revisar la sintaxis correcta en el archivo "Sintaxis_Webscraping.txt" para la correcta busqueda con el .select

#cuadro_texto = sopa.select('.tabs')
#print(cuadro_texto)
''' Al observar el output identifico que hay una clase dentro de la clase 'tabs' que contiene lo que busco, 
por lo que edito mi .select()   '''

cuadro_texto = sopa.select('.overflowable-item a')
print(cuadro_texto)

''' Hasta aqui hemos extraido los enlaces junto con sus nombres, ahora debemos extraer solo los enlaces '''

print("\n EXTRAYENDO LOS ENLACES:")
enlaces = [a['href'] for a in cuadro_texto] #'href' es el atributo que contiene el enlace(se encuentra dentro del html)
print(enlaces)

''' Si queremos extraer solo los nombres de los enlaces podemos hacer lo sigueinte: '''

print("\n EXTRAYENDO LOS NOMBRES DE LOS ENLACES:")
nombre_enlaces = [a.text for a in cuadro_texto]
print(nombre_enlaces)

''' En nuestra salida tenemos "||" ya que tenemos esa palabra con un href vacio asignado, de hecho,
 si observamos bien la lista de los enlaces extraidos, tenemos un elemnto vacio ("") en la posicion [1] de la lista
 Para arreglar esto podemos agregar un if para excluirlo.'''

print("\n EXTRAYENDO LOS ENLACES Y EXCLUYENDO EL ENLACE VACIO:")
enlaces = [a['href'] for a in cuadro_texto if a['href'] != '']
print(enlaces)

print("\n EXTRAYENDO LOS NOMBRES DE LOS ENLACES Y EXCLUYENDO EL ENLACE VACIO:")
nombre_enlaces = [a.text for a in cuadro_texto if a['href'] != '']
print(nombre_enlaces)



