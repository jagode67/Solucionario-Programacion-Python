import tkinter as tk
from tkinter import ttk

def avanzar():
    barra['value'] = 0
    incrementar()

def incrementar():
    if barra['value'] < 100:
        barra['value'] += 5
        ventana.after(100, incrementar)  # Llama de nuevo tras 100 ms

ventana = tk.Tk()
ventana.title("Progreso automático")

barra = ttk.Progressbar(ventana, orient="horizontal", length=300, mode="determinate", maximum=100)
barra.pack(pady=20)

boton = ttk.Button(ventana, text="Iniciar", command=avanzar)
boton.pack(pady=10)

ventana.mainloop()
