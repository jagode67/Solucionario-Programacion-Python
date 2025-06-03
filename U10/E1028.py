import tkinter as tk
from tkinter import scrolledtext

ventana = tk.Tk()
scrolled = scrolledtext.ScrolledText(ventana, width=40, height=10)
scrolled.pack(padx=10, pady=10)
ventana.mainloop()
