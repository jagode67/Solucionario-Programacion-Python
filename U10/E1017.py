import tkinter as tk
def cambiar():
    var.set("Nuevo valor")
ventana = tk.Tk()
var = tk.StringVar()
entrada = tk.Entry(ventana, textvariable=var)
entrada.pack()
boton = tk.Button(ventana, text="Cambiar valor", command=cambiar)
boton.pack()
ventana.mainloop()
