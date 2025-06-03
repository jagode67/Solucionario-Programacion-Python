import tkinter as tk
def insertar():
    texto.insert(tk.END, "Hola, mundo\n")
ventana = tk.Tk()
texto = tk.Text(ventana, width=30, height=5)
texto.pack()
boton = tk.Button(ventana, text="Insertar", command=insertar)
boton.pack()
ventana.mainloop()
