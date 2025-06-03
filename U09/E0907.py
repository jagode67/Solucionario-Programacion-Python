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
    
    # Solicitar la edad por pantalla
    edad_buscar = int(input("Introduce una edad: "))
    
    # Ejecutar la consulta SQL
    consulta = "SELECT id, nombre, edad FROM usuarios WHERE edad > %s"
    cursor.execute(consulta, (edad_buscar,))
    
    # Obtener y mostrar los resultados
    resultados = cursor.fetchall()
    
    if resultados:
        print("\nUsuarios mayores de", edad_buscar, "años:")
        print("ID\tNombre\t\tEdad")
        print("-" * 30)
        for (id, nombre, edad) in resultados:
            print(f"{id}\t{nombre}\t\t{edad}")
    else:
        print(f"\nNo hay usuarios mayores de {edad_buscar} años.")

except mysql.connector.Error as error:
    print("Error al conectar con MySQL:", error)

except ValueError:
    print("Error: Debes introducir un número válido para la edad.")

finally:
    # Cerrar la conexión
    if 'conexion' in locals() and conexion.is_connected():
        cursor.close()
        conexion.close()
        print("\nConexión a MySQL cerrada.")