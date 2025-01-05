#El Menu es un widget que proporciona una barra de menú en la parte superior de la ventana.
#Un menú puede contener submenús, que a su vez pueden contener otros submenús.

import tkinter as tk
root = tk.Tk()
root.minsize(300,300)
root.geometry("500x500")
root.title("Let's make a menu")

#-------------------------Creación de un menú-------------------------

#El Main Menu empezará aquí
mainmenu = tk.Menu(root)    #Esto será la barra de menú en la ventana
#Se crea un widget de menú en la ventana root y se guarda en la variable mainmenu.

#-------------------------Creación del menú File-------------------------

#Se crea un widget de menú y se guarda en la variable filemenu. 
filemenu = tk.Menu(mainmenu, tearoff=0) 
# 'mainmenu' indica que el menú filemenu será un submenú de mainmenu
# 'tearoff=0' se usa para que el menú no se pueda separar de la ventana. En caso contrario se usa 1.

#Se añaden los comandos (opciones) al menu guardado en la variable filemenu (en este caso los comandos son puros strings).
filemenu.add_command(label="New Text File") 
filemenu.add_command(label="New File")
filemenu.add_command(label="New Window")
filemenu.add_separator() #Esto se usa para separar los comandos en el menú
filemenu.add_command(label="Open File")
filemenu.add_command(label="Open Folder")

#Se agrega en la barra de menú 'mainmenu' la etiqueta 'File' que contendrá el menú 'filemenu'
mainmenu.add_cascade(label="File", menu=filemenu) 

#-------------------------Creación del submenú Open Recent en menú File-------------------------

openrecent = tk.Menu(filemenu)  #Se creará un submenú llamado 'Open Recent'. 'filemenu' indica que será un submenú de filemenu.
#Se añaden los comandos al submenú 'Open Recent' (en este caso de ejemplo los comandos son puros strings).
openrecent.add_command(label="File1 04/01/2025")
openrecent.add_command(label="File2 03/01/2025")
openrecent.add_command(label="File3 01/01/2025")
openrecent.add_command(label="File4 02/01/2025")

filemenu.add_cascade(label="Open Recent", menu=openrecent)#Se agrega la etiqueta Open Recent en el menú File con las opciones del menú openrecent.
filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)#Se agrega la opción Exit en el menú File con el comando root.quit que cerrará la ventana.

#-------------------------Creación del menú Edit-------------------------

editmenu = tk.Menu(mainmenu, tearoff=0)

editmenu.add_command(label="Undo")
editmenu.add_command(label="Redo")
editmenu.add_separator()
editmenu.add_command(label="Cut")
editmenu.add_command(label="Copy")
editmenu.add_command(label="Paste")
editmenu.add_separator()
editmenu.add_command(label="Find")
editmenu.add_command(label="Replace")

mainmenu.add_cascade(label="Edit", menu=editmenu)

#-------------------------Creación del menú View-------------------------

viewmenu=tk.Menu(mainmenu, tearoff=0)

viewmenu.add_checkbutton(label="Terminal")
viewmenu.add_checkbutton(label="Explorer")
viewmenu.add_separator()
viewmenu.add_radiobutton(label="Menu")
viewmenu.add_radiobutton(label="Panel")
viewmenu.add_radiobutton(label="Outputs")
viewmenu.add_separator()
viewmenu.add_command(label="Problems")
viewmenu.add_command(label="Debug console")

mainmenu.add_cascade(label="View", menu=viewmenu)

root.config(menu=mainmenu)#Esto se usa para mostrar el menú en la ventana
root.mainloop()