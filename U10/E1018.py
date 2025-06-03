import tkinter as tk
ventana = tk.Tk()
img = tk.PhotoImage(file="imagen.png")
boton = tk.Button(ventana, text="Imagen", image=img, compound="left")
boton.pack()
ventana.mainloop()
