import tkinter as tk
from tkinter import messagebox

def confirmar():
    respuesta = messagebox.askyesno("Confirmar", "¿Desea continuar?")
    print("Respuesta:", respuesta)

ventana = tk.Tk()
boton = tk.Button(ventana, text="Confirmar", command=confirmar)
boton.pack(padx=20, pady=20)
ventana.mainloop()
