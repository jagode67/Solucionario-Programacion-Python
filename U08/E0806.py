def gestionar_archivo_nombres():
    # Escribir en el archivo
    try:
        nombre_archivo = "nombres.txt"
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            while True:
                nombre = input("Introduce un nombre (o 'salir' para terminar): ")
                if nombre.lower() == 'salir':
                    break
                archivo.write(nombre + "\n")
            print(f"Nombres guardados correctamente en '{nombre_archivo}'")
        
        # Leer el archivo
        print("\nNombres guardados:")
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            if contenido:
                print(contenido)
            else:
                print("El archivo está vacío.")
                
    except FileNotFoundError:
        print(f"Error: No se puede encontrar el archivo '{nombre_archivo}'")
    except PermissionError:
        print(f"Error: No tienes permisos para acceder al archivo '{nombre_archivo}'")
    except Exception as e:
        print(f"Error inesperado: {e}")

# Ejecutar la función
gestionar_archivo_nombres()