import json

def gestionar_inventario_json():
    try:
        # Crear datos de productos
        productos = [
            {"nombre": "Teclado", "precio": 49.99, "stock": 15},
            {"nombre": "Ratón", "precio": 29.99, "stock": 3},
            {"nombre": "Monitor", "precio": 199.99, "stock": 8},
            {"nombre": "Disco duro", "precio": 89.99, "stock": 2},
            {"nombre": "Memoria USB", "precio": 19.99, "stock": 4}
        ]
        
        # Guardar en JSON
        with open("inventario.json", "w", encoding="utf-8") as archivo:
            json.dump({"productos": productos}, archivo, ensure_ascii=False, indent=4)
        
        print("Archivo JSON creado correctamente.")
        
        # Leer JSON y mostrar productos con stock bajo
        with open("inventario.json", "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
            
        print("\nProductos con stock bajo (menor a 5):")
        for producto in datos["productos"]:
            if producto["stock"] < 5:
                print(f"- {producto['nombre']}: {producto['stock']} unidades (${producto['precio']})")
                
    except FileNotFoundError:
        print("Error: No se pudo encontrar el archivo.")
    except json.JSONDecodeError:
        print("Error: El archivo JSON no tiene un formato válido.")
    except Exception as e:
        print(f"Error inesperado: {e}")

# Ejecutar la función
gestionar_inventario_json()