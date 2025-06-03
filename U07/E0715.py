class Vehiculo:
    def __init__(self, marca, modelo, anio, kilometros):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.kilometros = kilometros
       
    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.anio}) - {self.kilometros} km"

v = Vehiculo("Toyota", "Corolla", 2020, 35000)
print(v)
