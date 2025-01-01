# Tamaño y Posicionamiento de la ventana Tkinter

import tkinter as tk
root = tk.Tk()
root.title("Size and Positioning")

window_width = 800  # Ancho de la ventana Tkinter en pixeles
window_height = 600 # Alto de la ventana Tkinter en pixeles

screen_width = root.winfo_screenwidth()    #Metodo para obtener el ancho de la pantalla de la computadora en pixeles
screen_height = root.winfo_screenheight()   #Metodo para obtener el alto de la pantalla de la computadora en pixeles

#Si queremos que nuestra ventana Tkinter aparezca en el centro de la pantalla, se hace lo siguiente:
center_x = int((screen_width - window_width)/2) #Se calcula el centro de la pantalla en el eje x
center_y = int((screen_height - window_height)/2)   #Se calcula el centro de la pantalla en el eje Y

#Se establece el tamaño y la posicion de la ventana Tkinter
#El metodo geometry() recibe un string con el formato "ancho X alto + posicion_x + posicion_y"
root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")


root.mainloop()