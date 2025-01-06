#El widget message es un widget que permite mostrar mensajes de texto en una ventana.
#La diferencia entre el widget Message y el widget Label es que el widget Message permite mostrar mensajes de texto 
# en varias líneas, mientras que el widget Label solo permite mostrar mensajes de texto en una línea.


import tkinter as tk
root = tk.Tk()
root.minsize(200,200)
root.title("Widget Text vs Label")
label = tk.Label(root, text= "Este es un mensaje de texto creado con un widget label y esta todo en una sola línea.").pack()
message = tk.Message(root, text= "Este es un mensaje de texto creado con un widget message y esta en varias líneas.").pack()
root.mainloop()
