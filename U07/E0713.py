class Estudiante:
    def __init__(self, nombre, notas):
        self.nombre = nombre
        self.notas = notas
    def media(self):
        return sum(self.notas) / len(self.notas)
    def aprobado(self):
        return self.media() >= 5

e = Estudiante("Carlos", [7, 8, 4])
print(e.media())
print(e.aprobado())
