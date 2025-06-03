from datetime import datetime

class Registro:
    def __init__(self):
        self.creacion = datetime.now()
        
        
r = Registro()
print(r.creacion.strftime("%Y-%m-%d %H:%M:%S"))  # 2025-06-12 13:32:10
