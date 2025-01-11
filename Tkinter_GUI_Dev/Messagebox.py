#El widget Messagebox es usado para mostrar un mensaje emergente.
import tkinter as tk
#Para poder crear un message box se tiene que importar el modulo messagebox
from tkinter import messagebox

root=tk.Tk()
root.title("Messagebox Application")
root.minsize(200,200)
root.geometry("500x500")

#Se crea un messagebox.showinfo con titulo 'Info' y un mensaje. Este aparecerá al iniciar el programa.
messagebox.showinfo("info", "Learning is fun and practicing is clever")

#Hay diferentes tipos de messagebox y que se pueden detonar con ciertas acciones como apretar un boton

#-----------------------------------------------------------------------------------------------------------

#messagebox.info con boton:
#Se crea la funcion para activar el mensaje de info

def info():
    messagebox.showinfo("Info","This is a info messagebox with some important information about...something")
    
#Se cera el boton con etiqueta 'Info' que detonará el menssagebox.showinfo
info_button=tk.Button(root, text="Info", bg="lightblue", cursor="hand2", command=info).pack(pady=5)

#-----------------------------------------------------------------------------------------------------------
#messagebox.showwarning
#Se crea la funcion para activar el mensaje de warning

def warning():
    messagebox.showwarning("Warning","This is a Warning messagebox about...something important")

#Se crea el boton con etiqueta warning que detonará el mensaje de warning
warning_button=tk.Button(root, text="Warning", bg="yellow", cursor="hand2", command=warning).pack(pady=5)

#-----------------------------------------------------------------------------------------------------------
#messagebox.showerror
#Se crea la funcion para activar el mensaje de error

def error():
    messagebox.showerror("Fatal Error", "A Fatal Error has been ocurred")

#Se crea el boton con etiqueta Error que detonará el mensaje de Fatal Error
error_button=tk.Button(root, text="Error", bg="red", cursor="hand2", command=error).pack(pady=5)

root.mainloop()