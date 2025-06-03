def calcular_nota_media():
    try:
        nombre_archivo = "estudiantes.csv"
        estudiantes = []
        
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            # Saltar la cabecera
            lineas = archivo.readlines()[1:]
            
            for i, linea in enumerate(lineas):
                try:
                    datos = linea.strip().split(",")
                    if len(datos) >= 3:
                        nombre = datos[0]
                        edad = int(datos[1])
                        nota = float(datos[2])
                        estudiantes.append({"nombre": nombre, "edad": edad, "nota": nota})
                    else:
                        print(f"Advertencia: Línea {i+2} con formato incorrecto.")
                except ValueError:
                    print(f"Advertencia: Error en los datos de la línea {i+2}.")
        
        if estudiantes:
            suma_notas = sum(estudiante["nota"] for estudiante in estudiantes)
            media = suma_notas / len(estudiantes)
            print(f"Nota media de la clase: {media:.2f}")
            print(f"Total de estudiantes: {len(estudiantes)}")
        else:
            print("No se encontraron datos válidos de estudiantes.")
            
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no existe.")
    except Exception as e:
        print(f"Error inesperado: {e}")

# Ejecutar la función
calcular_nota_media()