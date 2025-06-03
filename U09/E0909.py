import mysql.connector

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
        id_usuario = int(input("Introduce el ID del usuario a eliminar: "))
        
        # Verificar si el usuario existe
        consulta_verificacion = "SELECT id, nombre FROM usuarios WHERE id = %s"
        cursor.execute(consulta_verificacion, (id_usuario,))
        usuario = cursor.fetchone()
        
        if usuario:
            # Mostrar información del usuario y solicitar confirmación
            print(f"\nUsuario encontrado: ID={usuario[0]}, Nombre={usuario[1]}")
            confirmacion = input("¿Estás seguro de que deseas eliminar este usuario? (s/n): ")
            
            if confirmacion.lower() == 's':
                # Eliminar el usuario
                consulta_eliminar = "DELETE FROM usuarios WHERE id = %s"
                cursor.execute(consulta_eliminar, (id_usuario,))
                conexion.commit()
                print("\nUsuario eliminado correctamente.")
            else:
                print("\nOperación cancelada.")
        else:
            print(f"\nNo existe el usuario con id #{id_usuario}")
            
    except ValueError:
        print("Error: El ID debe ser un número entero.")

except mysql.connector.Error as error:
    print("Error al conectar con MySQL:", error)

finally:
    # Cerrar la conexión
    if 'conexion' in locals() and conexion.is_connected():
        cursor.close()
        conexion.close()
        print("\nConexión a MySQL cerrada.")