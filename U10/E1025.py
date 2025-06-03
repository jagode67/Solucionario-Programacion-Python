import tkinter as tk
from tkinter import messagebox

def acerca_de():
    messagebox.showinfo("Acerca de", "Programa de ejemplo con menús en Tkinter.")

ventana = tk.Tk()
menubar = tk.Menu(ventana)
ventana.config(menu=menubar)

filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Nuevo")
filemenu.add_command(label="Abrir")
filemenu.add_command(label="Guardar")
filemenu.add_separator()
filemenu.add_command(label="Salir", command=ventana.quit)
menubar.add_cascade(label="Archivo", menu=filemenu)

helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="Acerca de...", command=acerca_de)
menubar.add_cascade(label="Ayuda", menu=helpmenu)

ventana.mainloop()
