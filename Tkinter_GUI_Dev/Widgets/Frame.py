#El widget Frame es un contenedor para otros widgets.
#Es un widget rectangular que se puede usar para organizar otros widgets.
import tkinter as tk

root = tk.Tk()
root.title("Widgets in windows with frames")
root.minsize(300, 200)

frame=tk.Frame(root, bg="pink", width=400, height=400)  #Se crea un frame con un color de fondo rosa.
frame.pack()    #Se empaqueta el frame en la ventana principal.

#Se crea un label dentro del frame.
label = tk.Label(frame, text = "label in Tkinter  \n this is a text label :D ",
bg="green",font="calibri", wraplength = 500, padx=20, pady=30).pack()

#Se crean 3 radio buttons dentro del frame.
select_languaje = tk.IntVar()
select_languaje.set(0)  #Se establece un valor por defecto que indica cual opcion estará seleccionada por defecto.
for text, value in (["C#", 1], ["Python", 2], ["Java", 3]):
    radio_button = tk.Radiobutton(frame, text = text,
                                  value = value,
                                  variable=select_languaje,
                                  cursor="hand2",
                                  indicatoron=False,
                                  width=10)
    radio_button.pack()

root.mainloop()