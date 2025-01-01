#Este script utiliza Tkinter y Pillow para crear una interfaz grafica de usuario (GUI) que muestra una imagen redimensionada en una ventana.

#Para mostrar imagenes en Tkinter se requiere tener instalado el modulo 'Pillow'
#Para saber si se tiene instalado, usar en consola: pip list
#Para instalarlo, usar en consola: pip install Pillow
#Para este ejemplo es necesario tener el archivo image.JPG en la misma carpeta donde se encuentre Label_Image.py

import tkinter as tk
from PIL import Image, ImageTk  #PIL es el nombre del paquete que se usa para importar el modulo pillow

pika_raw_img = Image.open("pikachu.jpg")  # Creamos una variable que almacene nuestra imagen usando la funcion 'Image.open' que importamos de Pillow
pika_raw_img = pika_raw_img.resize((800,480)) #Cambiamos el tamaño de la imagen a 800 X 480 Pixeles (800 en eje 'X' y 480 en eje 'Y')
root = tk.Tk()      #Creamos la ventana de la aplicacion y la almacenamos en la variable 'root'
root.title("Pikachu y el llamado de la naturaleza")

pika_tk_img = ImageTk.PhotoImage(pika_raw_img) #Convertimos la imagen "cruda" en un objeto PhotoImage utilizable para tkinter. Se guarda en una variable.

label_img = tk.Label(root, image=pika_tk_img) #Creamos un widget 'Label' y lo almacenamos en la variable 'label_img'.
# 'image = pika_tk_img' / Atributo que usamos para agregar una imagen con formato PhotoImage al widget.

label_img.pack() #Mostramos nuestro widget 'label_img' en la aplicacion.
root.mainloop() #Iniciamos el bucle principal de la aplicacion.