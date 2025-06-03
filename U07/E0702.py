class Mascota:
    def __init__(self, nombre):
        self.nombre = nombre
    def nombre_mayusculas(self):
        return self.nombre.upper()
perro = Mascota("Sam")
print(perro.nombre)  # Sam
print(perro.nombre_mayusculas()) 
