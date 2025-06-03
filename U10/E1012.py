import tkinter as tk
def mostrar():
    print(texto.get("1.0", tk.END))
ventana = tk.Tk()
texto = tk.Text(ventana, width=30, height=5)
texto.pack()
boton = tk.Button(ventana, text="Mostrar contenido", command=mostrar)
boton.pack()
ventana.mainloop()
