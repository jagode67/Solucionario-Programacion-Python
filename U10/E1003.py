import tkinter as tk
def saludar():
    print("¡Hola, mundo!")
ventana = tk.Tk()
boton = tk.Button(ventana, text="Saludar", command=saludar)
boton.pack()
ventana.mainloop()
