import sqlite3

def buscar_libros(criterio, valor):
    try:
        with sqlite3.connect("biblioteca.db") as conexion:
            cursor = conexion.cursor()
            
            # Verificar el criterio de búsqueda
            if criterio.lower() == 'autor':
                sql = "SELECT * FROM libros WHERE autor LIKE ?"
                # Usar comodines para buscar coincidencias parciales
                cursor.execute(sql, (f"%{valor}%",))
            elif criterio.lower() == 'año':
                sql = "SELECT * FROM libros WHERE año = ?"
                cursor.execute(sql, (valor,))
            else:
                print("Criterio no válido. Use 'autor' o 'año'")
                return []
            
            # Recuperar resultados
            resultados = cursor.fetchall()
            return resultados
            
    except Exception as e:
        print(f"Error en la búsqueda: {e}")
        return []

# Función para mostrar los resultados
def mostrar_resultados(libros):
    if not libros:
        print("No se encontraron libros con ese criterio")
        return
    
    print("\n{:<5} {:<30} {:<25} {:<10} {:<10}".format("ID", "TÍTULO", "AUTOR", "AÑO", "DISPONIBLE"))
    print("-" * 80)
    
    for libro in libros:
        disponible = "Sí" if libro[4] else "No"
        print("{:<5} {:<30} {:<25} {:<10} {:<10}".format(
            libro[0], libro[1], libro[2], libro[3], disponible
        ))

# Pruebas de búsqueda
print("Búsqueda por autor:")
libros_cervantes = buscar_libros('autor', 'Cervantes')
mostrar_resultados(libros_cervantes)
print("\nBúsqueda por año:")
libros_1949 = buscar_libros('año', 1949)
mostrar_resultados(libros_1949)