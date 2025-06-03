import tkinter as tk
ventana = tk.Tk()
boton = tk.Button(ventana, text="Botón principal")
boton.pack()
def deshabilitar():
    boton.config(state="disabled")
def habilitar():
    boton.config(state="normal")
btn_des = tk.Button(ventana, text="Deshabilitar", command=deshabilitar)
btn_des.pack()
btn_hab = tk.Button(ventana, text="Habilitar", command=habilitar)
btn_hab.pack()
ventana.mainloop()
