import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
combo = ttk.Combobox(ventana, values=["Python", "Java", "C++"], state="readonly")
combo.pack(padx=20, pady=20)
ventana.mainloop()
