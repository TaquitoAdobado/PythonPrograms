#Canvas es un widget que permite dibujar figuras geeometricas en una ventana Tkinter.

import tkinter as tk
root = tk.Tk()
root.minsize(400, 400)
root.geometry("600x600")
root.title("Drawing with Canvas")

#Primero se crea un objeto Canvas, se le asigna un color de fondo y se establece un tamaño.
canvas = tk.Canvas(root, bg="blue", height=400, width=400)

#Para dibujar un cuadrado, se usa el metodo '.create_rectangle()' del objeto Canvas.
#Por lo que primero creamos una variable 'rect' que contiene las coordenadas y el tamaño del cuadrado. (X1, Y1, X2, Y2)
rect = 10,10, 150, 100  
#Los primeros dos valores son las coordenadas X e Y del punto superior izquierdo del cuadrado.
#Los siguientes dos valores son las coordenadas X e Y del punto inferior derecho del cuadrado
#Esto indica el tamaño del cuadrado siendo X2-X1 = 90 y Y2-Y1 = 90
#Por lo que el cuadrado tendrá un tamaño de 90x90 pixeles.
canvas.create_rectangle(rect, fill="red")   #Se dibuja el cuadrado en el objeto Canvas con el color de relleno rojo.

#Dibujando un cuadrado 50x50
square = 10, 110, 60, 160   #Se crean las coordenadas y el tamaño del cuadrado. (X2-x1 = 50, Y2-Y1 = 50), 50x50 pixeles.
canvas.create_rectangle(square, fill="green")

#Para dibujar un circulo, se usa el metodo '.create_oval()' del objeto Canvas.
oval = 170, 10, 220, 60 #Se crean las coordenadas y el tamaño del circulo. (X2-x1 = 50, Y2-Y1 = 50), 50x50 pixeles.
canvas.create_oval(oval, fill="yellow")   #Se dibuja el circulo en el objeto Canvas con el color de relleno amarillo.

#Para dibujar una linea se usa el metodo '.create_line()' del objeto Canvas.
line = 10,10, 150, 100  #Se crean las coordenadas de la linea. (X1, Y1, X2, Y2)
#Se puede extender la linea agregando mas coordenadas (X3, Y3, X4, Y4, ...)
canvas.create_line(line, fill="black")

#Para dibujar un arco se usa el metodo '.create_arc()' del objeto Canvas.
arc = 170, 10 ,220,60#Se usan las mismas coordenas del circulo para dibujar el arco.
canvas.create_arc(arc, fill="white", start=0, extent=90)   #El angulo de inicio es 0 y el angulo de extensión es 90.

#Para dibujar un pologono se usa el metood '.create_polygon()' del objeto Canvas.
polygon= 250,10, 400,100, 300,150   #Se crean las coordenadas de los vertices del poligono. Un poligono cuenta con al menos 3 vertices.
canvas.create_polygon(polygon, fill="purple")

canvas.pack()   #Se empaqueta el objeto Canvas en la ventana principal para que sea visible.

root.mainloop()