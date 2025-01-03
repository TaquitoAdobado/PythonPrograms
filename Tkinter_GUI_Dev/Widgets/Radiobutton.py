#El widget Radiobutton es un botón que permite al usuario seleccionar SOLO una opción de un conjunto de opciones.

import tkinter as tk

root = tk.Tk()
root.minsize(400, 200)
root.title("Radiobutton Widget")

label_text = tk.Label(root, text="Select your favorite programming language:").pack()

#Se crea una variable tkinter para enlazar los botones de radio.
select_languaje = tk.IntVar()
select_languaje.set(0)  #Se establece un valor por defecto que indica cual opcion estará seleccionada por defecto.

#Para usar el widget Radiobutton, es muy util integrar un bucle for para crear varios botones de radio.
#En este caso, se crean 3 botones de radio, a cada boton se le asigna un valor que diferencie a cada uno de los demás.
for text, value in (["C#", 1], ["Python", 2], ["Java", 3]):
    radio_button = tk.Radiobutton(root, text = text, value = value, variable=select_languaje).pack()

root.mainloop()