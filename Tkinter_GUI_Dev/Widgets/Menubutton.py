#El widget menubutton es un botón que despliega un menú cuando se presiona.

import tkinter as tk
root=tk.Tk()
root.minsize(200,200)
root.geometry("500x500")
root.title("Menubutton")


#Se crea el widget Menubutton y se guarda en la variable menubutton.
menubutton= tk.Menubutton(root, text="Abrir menu", relief="raised")

#Se crea un widget de menú, el cual estará dentro del Menubutton.
menubutton_menu=tk.Menu(menubutton, tearoff=0) #tearDown indica que el menú no se puede separar.

#Se añaden los comandos que contendrá el menubutton_menu.
menubutton_menu.add_command(label="Opción 1")
menubutton_menu.add_command(label="Opción 2")
menubutton_menu.add_command(label="Opción 3")
menubutton_menu.add_command(label="Opción 4")

menubutton.pack()   #Se empaqueta el menubutton para que sea visible en la ventana.
menubutton.config(menu=menubutton_menu) #Se configura el menubutton para que contenga las opciones de menubutton_menu.
root.mainloop()