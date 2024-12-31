#El widget label es usado para mostrar imagenes o texto
import tkinter as tk 

root =tk.Tk()
root.title("Label con texto")

# con .Label() creamos la etiqueta y dentro de los "()" agregamos los atributos que ésta tendrá.

label = tk.Label(root, text = "label in Tkinter aaaaaaaaaaaa \n afaifsasfiuasbfi asjfbasifaufs ",
bg="green",font="calibri", wraplength = 500, padx=20, pady=30)

# root /elegimos en donde estará el label.
# text='example' /elegimos el texto que contendrá el label.
# bg='green' /elegimos el color de fondo del label, en este ejemplo usamos verde.
# font='calibri' /elegimos la fuente del texto del label, en este ejemplo usamos calibri.
# wraplength=500 /ajusta el ancho que tendra el label, si el texto lo excede continua en la siguiente linea.
# padx = 20, pady = 30 /Ajustamos el tamaño del widget. Padx agrega n cantidad de pixeles horizontalmente y pady verticalmente.

label.pack()    #Permite mostrar el texto de nuestra label

root.mainloop()