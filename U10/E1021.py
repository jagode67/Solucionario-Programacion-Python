import tkinter as tk
from tkinter import messagebox

def mostrar_mensaje():
    messagebox.showinfo("Información", "Operación realizada correctamente")

ventana = tk.Tk()
boton = tk.Button(ventana, text="Mostrar mensaje", command=mostrar_mensaje)
boton.pack(padx=20, pady=20)
ventana.mainloop()
