import tkinter as tk
def copiar():
    texto.insert(tk.END, entrada.get() + "\n")
ventana = tk.Tk()
entrada = tk.Entry(ventana)
entrada.pack()
boton = tk.Button(ventana, text="Copiar a Text", command=copiar)
boton.pack()
texto = tk.Text(ventana, width=30, height=5)
texto.pack()
ventana.mainloop()
