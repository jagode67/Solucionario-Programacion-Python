import json
import os

class SistemaInventario:
    def __init__(self, archivo_json='inventario.json'):
        """Inicializa el sistema de inventario."""
        self.archivo_json = archivo_json
        self.inventario = self._cargar_inventario()
    
    def _cargar_inventario(self):
        """Carga el inventario desde el archivo JSON. Si no existe, crea uno vacío."""
        if os.path.exists(self.archivo_json):
            try:
                with open(self.archivo_json, 'r') as archivo:
                    return json.load(archivo)
            except json.JSONDecodeError:
                print(f"Error al leer el archivo {self.archivo_json}. Creando inventario vacío.")
                return []
        else:
            return []
    
    def _guardar_inventario(self):
        """Guarda el inventario en el archivo JSON."""
        with open(self.archivo_json, 'w') as archivo:
            json.dump(self.inventario, archivo, indent=4)
    
    def añadir_producto(self, codigo, nombre, precio, cantidad):
        """Añade un nuevo producto al inventario."""
        # Verificar si el producto ya existe
        for producto in self.inventario:
            if producto['codigo'] == codigo:
                print(f"El producto con código {codigo} ya existe.")
                return False
        
        # Crear nuevo producto
        nuevo_producto = {
            'codigo': codigo,
            'nombre': nombre,
            'precio': float(precio),
            'cantidad': int(cantidad)
        }
        
        # Añadir al inventario
        self.inventario.append(nuevo_producto)
        self._guardar_inventario()
        print(f"Producto '{nombre}' añadido correctamente.")
        return True
    
    def buscar_producto(self, codigo=None, nombre=None):
        """Busca un producto por código o nombre."""
        productos_encontrados = []
        
        if codigo is not None:
            for producto in self.inventario:
                if producto['codigo'] == codigo:
                    productos_encontrados.append(producto)
                    break
        
        elif nombre is not None:
            nombre = nombre.lower()
            for producto in self.inventario:
                if nombre in producto['nombre'].lower():
                    productos_encontrados.append(producto)
        
        if not productos_encontrados:
            print("No se encontraron productos con esos criterios.")
        
        return productos_encontrados
    
    def actualizar_stock(self, codigo, nueva_cantidad):
        """Actualiza la cantidad en stock de un producto."""
        for producto in self.inventario:
            if producto['codigo'] == codigo:
                producto['cantidad'] = int(nueva_cantidad)
                self._guardar_inventario()
                print(f"Stock del producto {producto['nombre']} actualizado a {nueva_cantidad}.")
                return True
        
        print(f"No se encontró ningún producto con el código {codigo}.")
        return False
    
    def mostrar_inventario(self):
        """Muestra todo el inventario."""
        if not self.inventario:
            print("El inventario está vacío.")
            return
        
        print("\n=== INVENTARIO ACTUAL ===")
        print(f"{'CÓDIGO':<10} {'NOMBRE':<30} {'PRECIO':<10} {'CANTIDAD':<10}")
        print("=" * 60)
        
        for producto in self.inventario:
            print(f"{producto['codigo']:<10} {producto['nombre']:<30} {producto['precio']:<10.2f} {producto['cantidad']:<10}")


def menu_principal():
    """Muestra el menú principal y gestiona la interacción con el usuario."""
    sistema = SistemaInventario()
    
    while True:
        print("\n=== SISTEMA DE GESTIÓN DE INVENTARIO ===")
        print("1. Añadir producto")
        print("2. Buscar producto")
        print("3. Actualizar stock")
        print("4. Mostrar inventario")
        print("5. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            codigo = input("Código del producto: ")
            nombre = input("Nombre del producto: ")
            
            precio_valido = False
            while not precio_valido:
                try:
                    precio = float(input("Precio del producto: "))
                    precio_valido = True
                except ValueError:
                    print("Por favor, ingrese un precio válido.")
            
            cantidad_valida = False
            while not cantidad_valida:
                try:
                    cantidad = int(input("Cantidad en stock: "))
                    cantidad_valida = True
                except ValueError:
                    print("Por favor, ingrese una cantidad válida.")
            
            sistema.añadir_producto(codigo, nombre, precio, cantidad)
        
        elif opcion == "2":
            print("\n=== BUSCAR PRODUCTO ===")
            print("1. Buscar por código")
            print("2. Buscar por nombre")
            
            opcion_busqueda = input("\nSeleccione una opción: ")
            
            if opcion_busqueda == "1":
                codigo = input("Ingrese el código del producto: ")
                productos = sistema.buscar_producto(codigo=codigo)
            elif opcion_busqueda == "2":
                nombre = input("Ingrese el nombre (o parte) del producto: ")
                productos = sistema.buscar_producto(nombre=nombre)
            else:
                print("Opción no válida.")
                continue
            
            # Mostrar resultados
            if productos:
                print("\n=== RESULTADOS DE LA BÚSQUEDA ===")
                print(f"{'CÓDIGO':<10} {'NOMBRE':<30} {'PRECIO':<10} {'CANTIDAD':<10}")
                print("=" * 60)
                
                for producto in productos:
                    print(f"{producto['codigo']:<10} {producto['nombre']:<30} {producto['precio']:<10.2f} {producto['cantidad']:<10}")
        
        elif opcion == "3":
            codigo = input("Ingrese el código del producto a actualizar: ")
            try:
                nueva_cantidad = int(input("Ingrese la nueva cantidad en stock: "))
                sistema.actualizar_stock(codigo, nueva_cantidad)
            except ValueError:
                print("Por favor, ingrese una cantidad válida.")
        
        elif opcion == "4":
            sistema.mostrar_inventario()
        
        elif opcion == "5":
            print("Gracias por usar el Sistema de Gestión de Inventario. ¡Hasta pronto!")
            break
        
        else:
            print("Opción no válida. Por favor, intente de nuevo.")


if __name__ == "__main__":
    menu_principal()