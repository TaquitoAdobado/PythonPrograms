#El List Box es un widget que permite al usuario seleccionar uno o más elementos de una lista de elementos.

import tkinter as tk
root = tk.Tk()
root.minsize(200, 200)
root.geometry("400x400")
root.title("List Box Widget")
label = tk.Label(root, text="Display a list of items").pack()

listbox =tk.Listbox(root, width=30, selectbackground="green", height=10,justify="left", cursor="hand2", selectmode="multiple")


for item in range (1,11):
    listbox.insert("end", item)

listbox.pack()
root.mainloop()

#Los diferentes parametros que se pueden utilizar en el List Box son:
# width: Ancho del List Box.
# height: Altura del List Box.
# selectbackground: Color de fondo de los elementos seleccionados.
# justify: Alineación del texto en los elementos.
# cursor: Tipo de cursor.
# selectmode: Modo de selección de los elementos. Puede ser single, browse, multiple, extended.
# Para insertar elementos en el List Box, se utiliza el método insert().
# Para obtener los elementos seleccionados, se utiliza el método curselection().
# Para obtener el elemento seleccionado, se utiliza el método get().
# Para borrar un elemento, se utiliza el método delete().
# Para borrar todos los elementos, se utiliza el método delete(0, END).
# Para obtener el número de elementos, se utiliza el método size().
# Para obtener el índice de un elemento, se utiliza el método index().