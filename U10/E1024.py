import tkinter as tk

ventana = tk.Tk()
menubar = tk.Menu(ventana)
ventana.config(menu=menubar)

filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Salir", command=ventana.quit)
menubar.add_cascade(label="Archivo", menu=filemenu)

ventana.mainloop()
