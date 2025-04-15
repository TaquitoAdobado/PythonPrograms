'''
El modulo re es un modulo que nos permite trabajar con expresiones regulares, esto significa que nos permite
realizar busquedas en cadenas de texto mediante patrones que nosotros queramos.
'''

#Expresiones Regulares
''' antes de saber como realizar busquedas, debemos saber cuales son las regex (Expresiones Regulares):
\d = cualquier digito
\D = cualquier caracter no digito
\w = cualquier caracter alfanumerico
\W = cualquier caracter no alfanumerico
\s = cualquier espacio en blanco
\S = cualquier caracter no espacio en blanco
. = cualquier caracter
^ = comienza con
$ = termina con
+ = 1 o mas caracteres
* = 0 o mas repeticiones
? = 0 o 1 repeticion opcional
{m} = m repeticiones
{m,n} = m a n repeticiones'''

#Como usarlas
import re
texto = "mis codigos de seguridad son: 123-abc-1b3c y 321-cba-c3b1"

#El patron a buscar debe estar escrito de la siguiente manera: r'patron'
patron = r'\d{3}-\D{3}-\w{4}'   # "3 digitos", "-", "3 caracter no digitos", "-", "4 caracteres alfanumericos"

#re.search(patron, texto) busca el primer patron encontrado en el texto
print(re.search(patron, texto))

#Si la busqueda es exitosa devuelve un objeto de la clase Match, de lo contrario devuelve None
#output: <re.Match object; span=(27, 39), match='123-abc-1b3c'>
# Se nos indica que hay match desde el caracter 27 hasta el 39 y el match es '123-abc-1b3c'

#re.findall(patron, texto) busca todos los patrones encontrados y los devuelve dentro de una lista
print(re.findall(patron, texto))
#output:['123-abc-1b3c', '321-cba-c3b1']

'''
Al buscar un patron si se quiere buscar algun caracter, pero éste esta dentro de las expresiones regulares
se debe colocar despues de un \ para poder reconocerlo
'''

texto_2 = "mi red social favorita es: facebook.com"   #el punto es una expresion regular
patron_2 = r'\w+\.\w+'
#\w+ = 1 o mas caracteres alfanumericos
#\.\w+ = un punto seguido de 1 o mas caracteres alfanumericos

print(re.search(patron_2, texto_2))

''' existen multiples soluciones de acuerdo al patron buscado, usa la que mas se adapte a tu caso, por ejemplo:
patron_2 = r'\D+\.com' 

'''
