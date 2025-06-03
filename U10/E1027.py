import tkinter as tk
from tkinter import ttk

def on_tab_changed(event):
    tab = event.widget.tab(event.widget.index("current"), "text")
    print("Pestaña seleccionada:", tab)

ventana = tk.Tk()
notebook = ttk.Notebook(ventana)
notebook.pack(expand=1, fill='both')
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
notebook.add(tab1, text="Inicio")
notebook.add(tab2, text="Configuración")
notebook.bind("<<NotebookTabChanged>>", on_tab_changed)

ventana.mainloop()
