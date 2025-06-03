class Tienda:
    def __init__(self,*args):
        self.productos = []
        for p in args:
            self.productos.append(p)
        
mi_tienda = Tienda("Leche", "Pan", "Huevos")
print(mi_tienda.productos)  # ['Leche', 'Pan', 'Huevos']

