#El widget 'Entry' es usado para crear un campo de entrada para el usuario.
#Puede estar desbloqueada para que el usuario ingrese algo o bloqueada para que se muestre un mensaje inmodificable.

import tkinter as tk
root = tk.Tk()
root.title("Entry Widget")

label = tk.Label(root, text="Name: ")   #Se crea widget de texto que diga "Name: "
unblocked_entry = tk.Entry(root)  #Se crea el widget del campo de entrada desbloqueado, tambien se puede escribir como '(root, state="")'
blocked_entry = tk.Entry(root, state="disabled")

#Para mostrar un mensaje dentro de un campo desbloquedo se hace lo siguiente:
unblocked_entry.insert(0, "Unblocked")  #El 0 indica la posicion del texto (al inicio del campo)

#Para mostrar un mensaje dentro de un campo blqueado, primero se crea el widget, luego se agrega el texto y luego se bloquea el estado del widget:
text_blocked_entry = tk.Entry(root)
text_blocked_entry.insert(0, "blocked!!!")
text_blocked_entry.config(state="disabled")

label.pack()                #Se muestra el widget 'label'
unblocked_entry.pack()      #Se muestra el widget 'unblocked_entry'
blocked_entry.pack()        #Se muestra el widget 'blocked_entry'
text_blocked_entry.pack()   #Se meustra el widget 'text_blocked_entry'


root.mainloop()