import tkinter as tk
ventana = tk.Tk()
etiqueta = tk.Label(ventana, text="Etiqueta")
etiqueta.pack(side=tk.TOP, fill=tk.X)
boton = tk.Button(ventana, text="Izquierda")
boton.pack(side=tk.LEFT)
entrada = tk.Entry(ventana)
entrada.pack(side=tk.RIGHT, fill=tk.Y)
ventana.mainloop()
