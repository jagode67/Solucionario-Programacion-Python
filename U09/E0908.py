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
    
    while True:
        # Solicitar datos al usuario
        nombre = input("\nIntroduce el nombre (escribe 'fin' para terminar): ")
        
        # Verificar si el usuario quiere terminar
        if nombre.lower() == 'fin':
            break
            
        try:
            edad = int(input("Introduce la edad: "))
            
            # Preparar y ejecutar la consulta SQL de inserción
            consulta = "INSERT INTO usuarios (nombre, edad) VALUES (%s, %s)"
            valores = (nombre, edad)
            cursor.execute(consulta, valores)
            conexion.commit()
            
            print("Registro insertado correctamente.")
            
        except ValueError:
            print("Error: La edad debe ser un número entero.")
            continue

except mysql.connector.Error as error:
    print("Error al conectar con MySQL:", error)

finally:
    # Cerrar la conexión
    if 'conexion' in locals() and conexion.is_connected():
        cursor.close()
        conexion.close()
        print("\nConexión a MySQL cerrada.")