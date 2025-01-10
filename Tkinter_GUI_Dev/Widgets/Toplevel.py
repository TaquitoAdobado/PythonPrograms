#El widget toplevel sirve para crear ventanas adicionales

import tkinter as tk
root=tk.Tk()
root.geometry("500x500")
root.title("TopLevel Widget")
click_me_window=None

#Definimos una funcion en la que se cree un widget toplevel al clicar sobre un boton.
def c_window():
    global click_me_window  #Se define la variable global 'click_me_window
    click_me_window=tk.Toplevel(root)   #Se le asigna el widget toplevel en root
    #Se crea un widget de mensaje que aparecerá en el widget toplevel
    message = tk.Message(click_me_window, width=500,
    text="so you had clicked the button hmmm?\n this is a new window created by a toplevel widget :D").pack()
    #Se le agregan 2 botones con ciertas funciones(agree() y disagree()) que arrojan un mensaje y cierran el widget toplevel.
    radio=tk.Radiobutton(click_me_window, text="Agree to give your rights >:D",command=agree, value=1).pack()
    radio=tk.Radiobutton(click_me_window, text="disagree", command=disagree, value=1).pack()

def agree():
    tk.Label(root,text="thanks for your rights, dog!").pack()
    click_me_window.destroy()

def disagree():
    tk.Label(root, text="you had clicked disagree!?, well thats ok").pack()
    click_me_window.destroy()

#Se crea el boton en la ventana root que contiene la funcion que activa el widget toplevel
button=tk.Button(root, text="Click me!!!", cursor="hand2", bg="lightblue", activebackground="lightgreen",command=c_window).pack()

root.mainloop()