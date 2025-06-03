import sqlite3

def insertar_libros(libros_lista):
    try:
        with sqlite3.connect("biblioteca.db") as conexion:
            cursor = conexion.cursor()
            
            # Sentencia SQL con marcadores de posición
            sql = "INSERT INTO libros (titulo, autor, año, disponible) VALUES (?, ?, ?, ?)"
            
            # Ejecutar la inserción múltiple
            cursor.executemany(sql, libros_lista)
            
            # Confirmar cambios
            conexion.commit()
            
            return cursor.rowcount  # Devuelve el número de filas afectadas
            
    except Exception as e:
        print(f"Error al insertar libros: {e}")
        return 0

libros = [
    ("Don Quijote de la Mancha", "Miguel de Cervantes", 1605, True),
    ("Cien años de soledad", "Gabriel García Márquez", 1967, True),
    ("El Hobbit", "J.R.R. Tolkien", 1937, False),
    ("1984", "George Orwell", 1949, True)
]
registros_insertados = insertar_libros(libros)
print(f"Se insertaron {registros_insertados} libros en la base de datos")