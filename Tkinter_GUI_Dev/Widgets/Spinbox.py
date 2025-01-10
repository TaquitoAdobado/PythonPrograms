#El Spinbox widget crea un campo de entrada en el que se puede aumentar y disminuir un valor de un rango determinado
#Haciendo uso de flechas
import tkinter as tk
root=tk.Tk()
root.geometry("500x500")
root.minsize(200,200)
root.title("SpinBox Widget")

tk.Spinbox(root, from_=0, to=10).pack()
root.mainloop()