import tkinter as tk
from tkinter import ttk

def avanzar():
    barra.step(20)

ventana = tk.Tk()
barra = ttk.Progressbar(ventana, orient="horizontal", length=200, mode="determinate", maximum=100)
barra.pack(pady=20)
boton = ttk.Button(ventana, text="Avanzar", command=avanzar)
boton.pack()
ventana.mainloop()
