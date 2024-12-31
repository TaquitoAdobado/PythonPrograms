#Este script utiliza Tkinter y Pillow para crear una interfaz grafica de usuario (GUI) que muestra una imagen redimensionada en una ventana.

#Para mostrar imagenes en Tkinter se requiere tener instalado el modulo 'Pillow'
#Para saber si se tiene instalado, usar en consola: pip list
#Para instalarlo, usar en consola: pip install Pillow
#Para este ejemplo es necesario tener el archivo image.JPG en la misma carpeta donde se encuentre Label_Image.py


import tkinter as tk
from PIL import Image, ImageTk  #PIL es el nombre del paquete que se usa para importar el modulo pillow

image = Image.open("image.jpg")  # Creamos una variable que almacene nuestra imagen usando la funcion 'Image.open' que importamos de Pillow
image = image.resize((800,480)) #Cambiamos el tamaño de la imagen a 800 X 480 Pixeles (800 en eje 'X' y 480 en eje 'Y')
root = tk.Tk()      #Creamos la ventana de la aplicacion y la almacenamos en la variable 'root'
root.title("Pikachu y el llamado de la naturaleza")

img = ImageTk.PhotoImage(image) #Convierte nuestra imagen en un objeto PhotoImage que será usable en la aplicación. Se guarda en la varibale 'img'
label = tk.Label(root, image=img) #Creamos un widget 'Label y lo almacenamos en la variable 'label'. cargamos la imagen usando el atributo 'image'
label.pack() #Mostramos nuestro widget 'label' en la aplicacion.


root.mainloop() #Iniciamos el bucle principal de la aplicacion.
