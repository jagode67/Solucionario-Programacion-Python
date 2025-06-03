import datetime
actual = datetime.date.today().year
contador = 0
for i in range(5):
    fecha_str = input(f"Introduce la fecha {i+1} (AAAA-MM-DD): ")
    fecha = datetime.datetime.strptime(fecha_str, "%Y-%m-%d").date()
    if fecha.year == actual:
        contador += 1
print("Fechas del año actual:", contador)

