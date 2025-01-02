#Un boton es un widget que se usa para realizar acciones cuando se presiona.

import tkinter as tk

root = tk.Tk()
root.title("Button Widget")

#Para crear un boton, se usa la clase 'Button' y se almacena en una variable.
btn = tk.Button(root, text="Push me", fg="white", bg="blue", font=("Arial", 9), width=10, height=2,
relief="raised", state="normal", cursor="hand2", anchor="center", justify="center",
takefocus=True, wraplength=100, activebackground="red", activeforeground="white",
disabledforeground="gray", highlightbackground="black", highlightcolor="yellow",
highlightthickness=2, overrelief="sunken", repeatdelay=1000, repeatinterval=500, underline=0)

btn.pack()

root.mainloop()
#Los parametros que se pueden usar son:
#   - master: Es el widget padre del boton: root, frame, etc.
#   - text: Es el texto que se muestra en el boton: "Push me".
#   - command: Es la funcion que se ejecuta cuando se presiona el boton: funcion().    
#   - fg: Es el color del texto del boton: "white".
#   - bg: Es el color del fondo del boton: "blue".
#   - font: Es la fuente del texto del boton: "Arial", 9.
#   - width: Es el ancho del boton: 10.
#   - height: Es el alto del boton: 2.
#   - padx: Es el espacio horizontal entre el texto y los bordes del boton: 0.
#   - pady: Es el espacio vertical entre el texto y los bordes del boton: 0.
#   - relief: Es el tipo de borde que tiene el boton: "flat", "groove", "raised", "ridge", "solid", o "sunken".
#   - state: Es el estado del boton: "normal", "active", o "disabled".
#   - underline: Es el indice del caracter subrayado en el texto del boton: 0.
#   - image: Es la imagen que se muestra en el boton: img.
#   - compound: Es la posicion de la imagen en relacion al texto del boton: "top", "bottom", "left", o "right".
#   - cursor: Es el tipo de cursor que se muestra cuando el mouse esta sobre el boton: "arrow", "hand2", "circle", "cross", "plus", "watch", etc.
#   - anchor: Es la posicion del texto en el boton: "center", "n", "ne", "e", "se", "s", "sw", "w", "nw".
#   - justify: Es la alineacion del texto en el boton: "left", "right", "center".
#   - takefocus: Es un valor booleano que indica si el boton puede recibir el foco navegando con el teclado: True, False.
#   - textvariable: Es una variable que almacena el texto del boton, util para actualizar el texto del boton mediante una funcion: var.
#   - variable: Es una variable que almacena el valor del boton.
#   - wraplength: Es el ancho maximo del texto del boton: 100.
#   - activebackground: Es el color de fondo del boton cuando esta activo: "red".
#   - activeforeground: Es el color del texto del boton cuando esta activo: "white".
#   - disabledforeground: Es el color del texto del boton cuando esta desactivado: "gray".
#   - highlightbackground: Es el color del borde del boton cuando no tiene foco: "black".
#   - highlightcolor: Es el color del borde del boton cuando tiene foco: "yellow".
#   - highlightthickness: Es el grosor del borde del boton: 2.
#   - overrelief: Es el tipo de borde que tiene el boton cuando el mouse esta sobre el boton: "flat", "groove", "raised", "ridge", "solid", o "sunken".
#   - repeatdelay: Es el tiempo de espera antes de que el boton comience a repetir la accion. Es en milisegundos.
#   - repeatinterval: Es el tiempo entre cada repeticion de la accion del boton: 500.