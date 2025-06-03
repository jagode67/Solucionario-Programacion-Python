import tkinter as tk
ventana = tk.Tk()
etiqueta = tk.Label(ventana, text="Etiqueta")
etiqueta.grid(row=0, column=0)
entrada = tk.Entry(ventana)
entrada.grid(row=1, column=0)
boton = tk.Button(ventana, text="Botón")
boton.grid(row=2, column=0)
ventana.mainloop()
