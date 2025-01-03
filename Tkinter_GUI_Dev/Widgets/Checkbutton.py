import tkinter as tk

root = tk.Tk()
root.title("Checkbutton Widget")
root.minsize(300,200)

label_text = tk.Label(root, text = "Select the options you want:").pack()

#Para crear un Checkbutton, se usa la clase 'Checkbutton' y se almacena en una variable.
chkbtn = tk.Checkbutton(root, text = "Money").pack()
chkbtn = tk.Checkbutton(root, text = "Love").pack()
chkbtn = tk.Checkbutton(root, text = "Friends").pack()
chkbtn = tk.Checkbutton(root, text = "Family").pack()
chkbtn = tk.Checkbutton(root, text = "Healt").pack()

root.mainloop()