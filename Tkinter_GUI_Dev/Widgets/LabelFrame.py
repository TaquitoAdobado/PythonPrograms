#El widget LabelFrame tiene la misma funcion que el widget frame, con la diferencia de que incluye un label

import tkinter as tk
root=tk.Tk()
root.minsize(200,200)
root.geometry("500x500")
root.title("LabelFrame widget")

#Creamos el widget LabelFrame en la ventana root y le asignamos el texto "Login".
#Como si hicieramos una seccion de inicio de sesion en este ejemplo (no funcional)
labelframe=tk.LabelFrame(root, text="Login", labelanchor="n")

#Agregamos un widget entry dentro del LabelFrame para ingresar un usuario .

entry_user=tk.Entry(labelframe, cursor="hand2")
entry_user.insert(0, "Username")

#Agregamos otro widget entry dentro del LabelFrame esta vez para ingresar una contraseña
entry_password=tk.Entry(labelframe, show="*", cursor="hand2")
entry_password.insert(0, "Password")

#Agregamos un button widget dentro del LabelFrame para iniciar sesion.
login_button=tk.Button(labelframe, text="Login", bg="lightgrey", cursor="hand2")

labelframe.pack()
entry_user.pack(pady=10)
entry_password.pack(pady=10)
login_button.pack()

root.mainloop()