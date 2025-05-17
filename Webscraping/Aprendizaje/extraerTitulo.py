#Extraer un Titulo de una pagina web usando las bibliotecas de Python: beautifulsoup4 y requests

import requests
import bs4

# Primero debemos hacer una busqueda del codigo fuente de la pagina y almacenarlo en una variable
url = 'https://escueladirecta-blog.blogspot.com/' 
busqueda = requests.get(url)

# Para poder ver y analizar el contenido (el cual será el codigo HTML de la pagina), podemos usar el metodo .text
#print(busqueda.text)

''' En este punto tendremos una maraña de texto de tipo string, y para buscar lo que necesitamos debemos 
hacer un parser de ese texto (transformar el tipo de datos a uno que podamos manipular), 
para eso usamos beautifulsoup4 '''

sopa = bs4.BeautifulSoup(busqueda.text, "lxml")
# lxml es el parser que usaremos para analizar el HTML

#print(sopa)
''' nos devuelve el código HTML de la pagina pero a diferencia de la busqueda con requests, podemos acceder a 
los elementos que necesitamos mediante las etiquetas del HTML. 
En este caso para extraer el titulo de la pagina debemos identificar el nombre de la etiqueta que contiene 
el titulo en este caso es "title"   '''

titulo = sopa.select("title")
print(titulo)   #Output: [<title>Escuela Directa - Blogspot</title>]
''' El resultado estará en formato de lista, ya que puede haber multiples etiquetas con el mismo nombre. '''

#Al ser de tipo lista, podemos usar todos los metodos de las listas.
print(titulo[0])    #Output: <title>Escuela Directa - Blogspot</title>

#Para acceder al texto sin la etiqueta, usamos el metodo .gettext()
print(titulo[0].getText())   #Output: Escuela Directa - Blogspot

