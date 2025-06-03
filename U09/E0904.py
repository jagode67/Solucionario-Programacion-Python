import sqlite3

def actualizar_disponibilidad(id_libro, disponible):
    try:
        with sqlite3.connect("biblioteca.db") as conexion:
            cursor = conexion.cursor()
            
            # Verificar si el libro existe
            cursor.execute("SELECT id FROM libros WHERE id = ?", (id_libro,))
            if not cursor.fetchone():
                print(f"Error: No existe un libro con ID {id_libro}")
                return False
            
            # Actualizar disponibilidad
            cursor.execute(
                "UPDATE libros SET disponible = ? WHERE id = ?", 
                (disponible, id_libro)
            )
            
            # Confirmar cambios
            conexion.commit()
            
            if cursor.rowcount > 0:
                estado = "disponible" if disponible else "no disponible"
                print(f"Libro con ID {id_libro} actualizado a {estado}")
                return True
            else:
                print(f"No se pudo actualizar el libro con ID {id_libro}")
                return False
                
    except Exception as e:
        print(f"Error al actualizar: {e}")
        return False

# Prueba de la función
actualizar_disponibilidad(3, True)  # Hacer disponible el libro con ID 3
actualizar_disponibilidad(99, False)  # ID que no existe