#El widget Pane sirve para crear contenedores divididos en paneles a los cuales se le pueden agregar otros widgets
import tkinter as tk
root=tk.Tk()
root.minsize(200,200)
root.geometry("500x500")
root.title("Dividing with Panes")

#S
panewindow=tk.PanedWindow(root, bg="black")
panewindow.pack()

label1=tk.Label(panewindow, text="Pane1")
panewindow.add(label1)
label2=tk.Label(panewindow, text="Pane2")
panewindow.add(label2)
label3=tk.Label(panewindow, text="Pane3")
panewindow.add(label3)

root.mainloop()