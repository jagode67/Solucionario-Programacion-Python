import sqlite3
import logging

# Configurar el archivo de log
logging.basicConfig(
    level=logging.INFO,
    filename='biblioteca.log',
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding="utf-8"
)

def eliminar_libro(id_libro):
    try:
        # Verificar si el libro existe
        with sqlite3.connect("biblioteca.db") as conexion:
            cursor = conexion.cursor()
            cursor.execute("SELECT titulo FROM libros WHERE id = ?", (id_libro,))
            libro = cursor.fetchone()
            
            if not libro:
                mensaje = f"Intento de eliminar un libro con ID {id_libro} que no existe"
                print(mensaje)
                logging.warning(mensaje)
                return False
            
            titulo = libro[0]
            
            # Confirmar eliminación
            confirmacion = input(f"¿Está seguro de eliminar el libro '{titulo}' (ID: {id_libro})? (s/n): ")
            if confirmacion.lower() != 's':
                mensaje = f"Eliminación del libro '{titulo}' (ID: {id_libro}) cancelada por el usuario"
                print(mensaje)
                logging.info(mensaje)
                return False
            
            # Eliminar el libro
            cursor.execute("DELETE FROM libros WHERE id = ?", (id_libro,))
            conexion.commit()
            
            mensaje = f"Libro '{titulo}' (ID: {id_libro}) eliminado correctamente"
            print(mensaje)
            logging.info(mensaje)
            return True
            
    except Exception as e:
        mensaje = f"Error al eliminar libro ID {id_libro}: {e}"
        print(mensaje)
        logging.error(mensaje)
        return False

# Prueba de la función
eliminar_libro(2)  # Eliminar el libro con ID 2