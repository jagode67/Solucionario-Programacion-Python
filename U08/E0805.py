def calcular_promedio_notas():
    try:
        # Leer el archivo
        with open("notas.txt", "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
        
        # Convertir las líneas a números
        notas = []
        for i, linea in enumerate(lineas):
            try:
                nota = float(linea.strip())
                notas.append(nota)
            except ValueError:
                print(f"Advertencia: La línea {i+1} no contiene un número válido.")
        
        # Calcular promedio
        if notas:
            promedio = sum(notas) / len(notas)
            
            # Guardar resultado
            with open("resultado.txt", "w", encoding="utf-8") as archivo_salida:
                archivo_salida.write(f"Promedio de notas: {promedio:.2f}\n")
                archivo_salida.write(f"Total de notas válidas: {len(notas)}")
            
            print(f"El promedio {promedio:.2f} ha sido guardado en 'resultado.txt'")
        else:
            print("No se encontraron notas válidas para calcular el promedio.")
            
    except FileNotFoundError:
        print("Error: El archivo 'notas.txt' no existe.")
    except Exception as e:
        print(f"Error inesperado: {e}")

# Ejecutar la función
calcular_promedio_notas()