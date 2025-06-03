

num_encuestados = int(input("¿Cuántas personas participarán en la encuesta? "))


nombres = []
calificaciones = []

for i in range(num_encuestados):
    nombre = input(f"Introduce el nombre de la persona {i+1}: ")
    calificacion=0

    while not(1 <= calificacion <= 5):
            calificacion = int(input(f"Introduce la calificación de satisfacción de {nombre} (1-5): "))
            if not (1 <= calificacion <= 5):
                print("Calificación fuera de rango. Debe estar entre 1 y 5.")
    nombres.append(nombre)
    calificaciones.append(calificacion)

# Calcular el promedio
promedio = sum(calificaciones) / num_encuestados

# Encontrar la(s) persona(s) más satisfecha(s)
max_calificacion = max(calificaciones)
mas_satisfechos = []
for i in range(len(calificaciones)):
    if calificaciones[i] == max_calificacion:
        mas_satisfechos.append(nombres[i])

# Encontrar la(s) persona(s) menos satisfecha(s)
min_calificacion = min(calificaciones)
menos_satisfechos = []
for i in range(len(calificaciones)):
    if calificaciones[i] == min_calificacion:
        menos_satisfechos.append(nombres[i])

print(f"\nResultados de la encuesta:")
print(f"Calificación promedio: {promedio:.2f}")  # Formatear a 2 decimales
print(f"Persona(s) más satisfecha(s) ({max_calificacion}): {', '.join(mas_satisfechos)}")
print(f"Persona(s) menos satisfecha(s) ({min_calificacion}): {', '.join(menos_satisfechos)}")



