#El widget scrollbar sirve para agregar barras de desplazamiento a otros widgets.
#Esto es util para widgets que contienen una gran cantidad de información y no se puede mostrar toda en la pantalla.
#Se puede agregar barras de desplazamiento horizontal y vertical.
#Se pueden agregar barras de desplazamiento a los siguientes widgets:
#- Canvas
#- Listbox
#- Text
#- Entry
#- Frame
#- Message

import tkinter as tk
root = tk.Tk()
root.geometry("400x400")
root.title("Scrollbar in List Box Widget")
label = tk.Label(root, text="Display a list of items").pack()

#--------------------------Creacion de Frame--------------------------------
frame=tk.Frame(root,)
#Se crea un widget Frame que contenga el widget Listbox con un widget Scrollbar.

#--------------------------Creacion listbox--------------------------------

listbox =tk.Listbox(frame, width=30, selectbackground="green", height=5,justify="left", cursor="hand2", selectmode="multiple")

for item in range (1,11):
    listbox.insert("end", item)

#--------------------------Creacion de scrollbar--------------------------------

scroll=tk.Scrollbar(frame, command=listbox.yview) 
#.yview significa que la barra de desplazamiento es vertical asignada al widget listbox.

#Se configura coloca la barra de desplazamiento en el widget listbox
listbox.config(yscrollcommand=scroll.set)


#------------------------Se empaquetan los widgets para que sean mostrados-----------------

scroll.pack(side="right", fill="y")
#Se configura la scrollbar con .pack para que se muestre en la ventana.
#side indica en que lado de la ventana se mostrará la barra de desplazamiento.
#fill indica que la barra de desplazamiento se ajuste al tamaño de la ventana en el eje y.
listbox.pack()
frame.pack()
root.mainloop()