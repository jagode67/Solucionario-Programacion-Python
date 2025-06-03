class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

class Empleado(Persona):
    def __init__(self, nombre, puesto):
        super().__init__(nombre)
        self.puesto = puesto

e = Empleado("Maria", "Desarrolladora")
print(e.puesto)  # Desarrolladora
