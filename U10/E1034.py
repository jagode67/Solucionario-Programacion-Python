import tkinter as tk
from tkinter import ttk

def comenzar():
    barra.start(10)

def detener():
    barra.stop()

ventana = tk.Tk()
barra = ttk.Progressbar(ventana, orient="horizontal", length=200, mode="indeterminate")
barra.pack(pady=20)
boton1 = ttk.Button(ventana, text="Comenzar", command=comenzar)
boton1.pack(side=tk.LEFT, padx=10)
boton2 = ttk.Button(ventana, text="Detener", command=detener)
boton2.pack(side=tk.LEFT, padx=10)
ventana.mainloop()
