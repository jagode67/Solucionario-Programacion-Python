import tkinter as tk
from tkinter import ttk, messagebox

def cambio(event):
    seleccion = combo.get()
    messagebox.showinfo("Nuevo elemento seleccionado", seleccion)

ventana = tk.Tk()
combo = ttk.Combobox(ventana, values=["Python", "Java", "C++"])
combo.pack()
combo.bind("<<ComboboxSelected>>", cambio)
ventana.mainloop()
