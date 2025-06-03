import tkinter as tk
from tkinter import messagebox

def advertencia():
    messagebox.showwarning("Advertencia", "¡Cuidado con esta acción!")

ventana = tk.Tk()
boton = tk.Button(ventana, text="Advertencia", command=advertencia)
boton.pack(padx=20, pady=20)
ventana.mainloop()
