
import datetime

class Evento:
    def __init__(self, nombre, fecha):
        self.nombre = nombre
        self.fecha = fecha
    def es_futuro(self):
        return self.fecha > datetime.date.today()

ev = Evento("Concierto", datetime.date(2025, 5, 1))
print(ev.es_futuro()) #false

