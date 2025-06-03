class Tienda:
    def __init__(self,*args):
        self.productos = []
        for p in args:
            self.productos.append(p)
    def existe_producto(self, producto):
        return producto in self.productos
        
mi_tienda = Tienda("Leche", "Pan", "Huevos")
print(mi_tienda.productos)  # ['Leche', 'Pan', 'Huevos']
print(mi_tienda.existe_producto("Pan"))  # True

