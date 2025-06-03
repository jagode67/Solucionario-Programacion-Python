import sqlite3

try:
    # Establecer conexión
    with sqlite3.connect("biblioteca.db") as conexion:
        # Crear cursor
        cursor = conexion.cursor()
        
        # Crear tabla libros
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS libros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL,
            año INTEGER,
            disponible BOOLEAN DEFAULT 1
        )
        ''')
        
        # Confirmar cambios
        conexion.commit()
        print("Tabla 'libros' creada correctamente")
        
except Exception as e:
    print(f"Error: {e}")