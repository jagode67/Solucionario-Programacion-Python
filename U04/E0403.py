estudiantes = []  # Lista para almacenar tuplas (nombre, calificacion)

while True:
    nombre = input("Introduce el nombre del estudiante (o 'fin' para terminar): ")
    if nombre.lower() == "fin":
        break
    try:
        calificacion = float(input(f"Introduce la calificación de {nombre}: "))
        estudiantes.append((nombre, calificacion))
    except ValueError:
        print("Calificación inválida. Por favor, introduce un número.")

# Ordenar la lista de estudiantes por calificación (de mayor a menor)
estudiantes.sort(key=lambda x: x[1], reverse=True)

print("\nLista de estudiantes y calificaciones (ordenada):")
for nombre, calificacion in estudiantes:
    print(f"{nombre}: {calificacion}")


