import tkinter as tk    #Se importa la libreria Tkinter y se le asigna el alias "tk" para usarlo en el codigo

root =tk.Tk()   #Se crea la ventana principal (main) de la aplicacion y se le asigna a la variable "root"
root.title("My first Tkinter application")  #Se define el titulo de la ventana main

root.minsize(400,400) #Se define el tamaño minimo de la ventana main en pixeles
# En este espacio entre el titulo y el mainloop se escribirá el codigo de los widgets que se mostraran en la ventana main

root.mainloop() #Inicia un loop infinito en el main que mantendrá actualizada la aplicacion por cualquier evento ocurrido en ella.