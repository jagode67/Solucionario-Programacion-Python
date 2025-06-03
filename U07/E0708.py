class Figura:
    def area(self):
        pass

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado
        
    def area(self):
        return self.lado ** 2

fig = Cuadrado(5)
print(fig.area())  # 25
