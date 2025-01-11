#El widget Messagebox es usado para mostrar un mensaje emergente.
import tkinter as tk
#Para poder crear un message box se tiene que importar el modulo messagebox
from tkinter import messagebox

root=tk.Tk()
root.title("Messagebox Application")
root.minsize(200,200)
root.geometry("500x500")

#Se crea un messagebox.showinfo con titulo 'Info' y un mensaje. Este aparecerá al iniciar el programa.
messagebox.showinfo("info", "Learning is fun and practicing is clever")

#Hay diferentes tipos de messagebox y que se pueden detonar con ciertas acciones como apretar un boton

#-----------------------------------------------------------------------------------------------------------

#messagebox.info con boton:
#Se crea la funcion para activar el mensaje de info

def info():
    messagebox.showinfo("Info","This is a info messagebox with some important information about...something")
    
#Se cera el boton con etiqueta 'Info' que detonará el menssagebox.showinfo
info_button=tk.Button(root, text="Info", bg="lightblue", cursor="hand2", command=info).pack(pady=5)

#-----------------------------------------------------------------------------------------------------------
#messagebox.showwarning
#Se crea la funcion para activar el mensaje de warning

def warning():
    messagebox.showwarning("Warning","This is a Warning messagebox about...something important")

#Se crea el boton con etiqueta warning que detonará el mensaje de warning
warning_button=tk.Button(root, text="Warning", bg="yellow", cursor="hand2", command=warning).pack(pady=5)

#-----------------------------------------------------------------------------------------------------------
#messagebox.showerror
#Se crea la funcion para activar el mensaje de error

def error():
    messagebox.showerror("Fatal Error", "A Fatal Error has been ocurred")

#Se crea el boton con etiqueta Error que detonará el mensaje de Fatal Error
error_button=tk.Button(root, text="Error", bg="red", cursor="hand2", command=error).pack(pady=5)

#-----------------------------------------------------------------------------------------------------------
#messagebox.askyesno
#Se crea un messagebox.askyesno el cual dara la opcion de elegir entre yes y no.
#Yes devolverá un estado True y No uno False, que usaremos para mostrar un mnsaje
answer_label=None #Como se usará esta variable en la funcion, debe declararse antes
def question():
    global answer_label
    msgbox_answer=messagebox.askyesno("Question 1", "Is this a question?")

#Si ya se tiene una etiqueta de respuesta se elimina
    if answer_label:
        answer_label.destroy()

#Se crean etiquetas de respuesta en caso de apretar Yes o No
    if msgbox_answer==True:
       answer_label= tk.Label(root, text="You had clicked Yes :D")
    else:
        answer_label= tk.Label(root, text="You had clicked No :c")
    answer_label.pack()

#Se crea boton de Question para detonar la ventana de pregunta
question_button=tk.Button(root, text="Question", cursor="hand2", bg="lightgreen", command=question).pack(pady=5)


root.mainloop()