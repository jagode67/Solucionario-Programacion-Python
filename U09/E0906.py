#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3
import json

def exportar_libros_a_json():
    """
    Exporta los libros de la base de datos a un archivo JSON.
    """
    try:
        # Conectar a la base de datos
        conn = sqlite3.connect('biblioteca.db')
        # Configurar para que las filas se devuelvan como diccionarios
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        # Consultar todos los libros
        cursor.execute("SELECT * FROM libros")
        print("Exportando todos los libros")
        
        # Obtener los resultados
        libros = [dict(row) for row in cursor.fetchall()]
        
        # Convertir valores booleanos adecuadamente
        for libro in libros:
            libro['disponible'] = bool(libro['disponible'])
        
        # Guardar en un archivo JSON con formato legible
        with open('libros.json', 'w', encoding='utf-8') as f:
            json.dump(libros, f, ensure_ascii=False, indent=4)
        
        print(f"Se han exportado {len(libros)} libros al archivo 'libros.json'")
        
    except sqlite3.Error as e:
        print(f"Error en la base de datos SQLite: {e}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if conn:
            conn.close()

# Ejecutar la función de exportación directamente
if __name__ == "__main__":
    exportar_libros_a_json()