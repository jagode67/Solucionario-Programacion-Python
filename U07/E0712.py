class Agenda:
    def __init__(self):
        self.contactos = {}
    def agregar(self, nombre, telefono):
        self.contactos[nombre] = telefono
    def buscar(self, nombre):
        return self.contactos.get(nombre, "No encontrado")
    def mostrar_todos(self):
        for nombre, tel in self.contactos.items():
            print(f"{nombre}: {tel}")

a = Agenda()
a.agregar("Carlos", "123")
a.agregar("Lara", "456")
print(a.buscar("Lara")) # 456
a.mostrar_todos()
