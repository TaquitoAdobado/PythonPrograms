#El widget Scale sirve para seleccionar un valor numérico dentro de un rango determinado.
# Este se representa como una barra deslizante.

import tkinter as tk
root= tk.Tk()
root.geometry("500x500")
root.title("Scale Widget")

#Se crea el widget Scale
scale=tk.Scale(root, from_=0, to=100, orient="horizontal", length=200, activebackground="green",bg="lightblue", bd=5,
cursor="hand2", troughcolor="red")
scale.pack()
root.mainloop()
#Los parametros que puede tener el widget Scale son:
# - activebackground: color de fondo cuando el cursor está sobre el widget
# - bg: color de fondo
# - troughcolor: color de la barra
# - bd: ancho del borde
# - from_: valor mínimo
# - to: valor máximo
# - orient: orientación del widget: horizontal o vertical
# - length: longitud del widget en píxeles
# - width: ancho del widget en pixeles
# - sliderlength: longitud del slider
# - cursor: tipo de cursor: hand2, arrow, circle, clock, cross, dotbox, exchange, fleur, heart
# - digits: número de decimales
# - fg: color del texto
# - font: fuente del texto
# - relief: tipo de borde: flat, groove, raised, ridge, solid, sunken
# - showvalue: mostrar el valor actual del widget en la barra: 0, 1
# - state: estado del widget
# - tickinterval: separación entre las marcas
# - variable: variable asociada al widget
# - takefocus: si el widget puede tomar el foco
# - command: función que se ejecuta cuando se cambia el valor del widget