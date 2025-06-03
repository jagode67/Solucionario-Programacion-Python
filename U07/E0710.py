class Libro:
    def __init__(self, titulo, autores):
        self.titulo = titulo
        self.autores = autores
    def mostrar(self):
        print(f"{self.titulo} - Autores: {', '.join(self.autores)}")

l = Libro("Python Básico", ["Ana", "Carlos", "Eva"])
l.mostrar()

