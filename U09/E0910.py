import mysql.connector
import logging
from datetime import datetime

# Configuración del logging
logging.basicConfig(
    filename='libros.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Configuración de la conexión a MySQL
conf = {
    'host': 'localhost',
    'user': 'root',
    'database': 'test'
}

try:
    # Establecer conexión con la base de datos
    conexion = mysql.connector.connect(**conf)
    cursor = conexion.cursor()
    
    # Solicitar el ID del usuario
    try:
        id_usuario = int(input("Introduce el ID del usuario a modificar: "))
        
        # Verificar si el usuario existe
        consulta_verificacion = "SELECT id, nombre FROM usuarios WHERE id = %s"
        cursor.execute(consulta_verificacion, (id_usuario,))
        usuario = cursor.fetchone()
        
        if usuario:
            # Mostrar información actual y solicitar nuevo nombre
            print(f"\nUsuario encontrado: ID={usuario[0]}, Nombre actual={usuario[1]}")
            nuevo_nombre = input("Introduce el nuevo nombre: ")
            
            # Actualizar el nombre del usuario
            consulta_actualizar = "UPDATE usuarios SET nombre = %s WHERE id = %s"
            cursor.execute(consulta_actualizar, (nuevo_nombre, id_usuario))
            conexion.commit()
            
            # Registrar en el log
            logging.info(f"Usuario modificado - ID: {id_usuario}, Nuevo nombre: {nuevo_nombre}")
            
            print("\nNombre actualizado correctamente.")
        else:
            print(f"\nNo existe el usuario con id #{id_usuario}")
            
    except ValueError:
        print("Error: El ID debe ser un número entero.")

except mysql.connector.Error as error:
    print("Error al conectar con MySQL:", error)
    logging.error(f"Error en la conexión MySQL: {error}")

finally:
    # Cerrar la conexión
    if 'conexion' in locals() and conexion.is_connected():
        cursor.close()
        conexion.close()
        print("\nConexión a MySQL cerrada.")