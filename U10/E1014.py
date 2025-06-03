import tkinter as tk
def resaltar():
    texto.tag_add("resaltado", "1.0", "1.4")
    texto.tag_config("resaltado", background="yellow")
ventana = tk.Tk()
texto = tk.Text(ventana, width=30, height=5)
texto.insert(tk.END, "Texto de ejemplo\n")
texto.pack()
boton = tk.Button(ventana, text="Resaltar", command=resaltar)
boton.pack()
ventana.mainloop()
