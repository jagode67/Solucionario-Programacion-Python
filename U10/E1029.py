import tkinter as tk
from tkinter import scrolledtext

def copiar():
    texto = scrolled1.get("sel.first", "sel.last")
    scrolled2.delete("1.0", tk.END)
    scrolled2.insert("1.0", texto)

ventana = tk.Tk()
scrolled1 = scrolledtext.ScrolledText(ventana, width=40, height=5)
scrolled1.pack()
scrolled2 = scrolledtext.ScrolledText(ventana, width=40, height=5)
scrolled2.pack()
boton = tk.Button(ventana, text="Copiar selección", command=copiar)
boton.pack(pady=5)
ventana.mainloop()
