import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
notebook = ttk.Notebook(ventana)
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
notebook.add(tab1, text="Inicio")
notebook.add(tab2, text="Configuración")
notebook.pack(expand=1, fill='both')

ttk.Label(tab1, text="Bienvenido a la pestaña de inicio").pack(pady=10)
ttk.Label(tab2, text="Opciones de configuración").pack(pady=10)

ventana.mainloop()
