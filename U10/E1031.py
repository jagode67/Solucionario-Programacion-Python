import tkinter as tk
from tkinter import ttk, messagebox

def mostrar():
    seleccion = combo.get()
    messagebox.showinfo("Selección", f"Has seleccionado: {seleccion}")

ventana = tk.Tk()
combo = ttk.Combobox(ventana, values=["Python", "Java", "C++"], state="readonly")
combo.pack()
boton = ttk.Button(ventana, text="Mostrar selección", command=mostrar)
boton.pack(pady=10)
ventana.mainloop()
