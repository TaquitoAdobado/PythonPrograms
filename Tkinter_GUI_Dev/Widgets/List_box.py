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