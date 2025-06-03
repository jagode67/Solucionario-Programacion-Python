import tkinter as tk
ventana = tk.Tk()
entrada_var = tk.StringVar()
entrada = tk.Entry(ventana, textvariable=entrada_var)
entrada.pack()
etiqueta = tk.Label(ventana, text="Texto aquí")
etiqueta.pack()
def actualizar():
    etiqueta.config(text=entrada_var.get())
boton = tk.Button(ventana, text="Actualizar", command=actualizar)
boton.pack()
ventana.mainloop()
