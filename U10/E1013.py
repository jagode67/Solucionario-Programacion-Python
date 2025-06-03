import tkinter as tk
def limpiar():
    texto.delete("1.0", tk.END)
ventana = tk.Tk()
texto = tk.Text(ventana, width=30, height=5)
texto.pack()
boton = tk.Button(ventana, text="Limpiar", command=limpiar)
boton.pack()
ventana.mainloop()
