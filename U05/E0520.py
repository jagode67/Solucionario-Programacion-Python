import datetime
fecha_str1 = input("Introduce una fecha 1 (DD-MM-AAAA): ")
fecha_str2 = input("Introduce una fecha 2 (DD-MM-AAAA): ")

# Convert string dates to datetime objects
fecha1 = datetime.datetime.strptime(fecha_str1, "%d-%m-%Y")
fecha2 = datetime.datetime.strptime(fecha_str2, "%d-%m-%Y")

# Calculate difference between dates
diferencia = fecha2 - fecha1

# Convert difference to hours
horas = diferencia.total_seconds() / 3600

print(f"Entre las dos fechas hay {abs(horas)} horas")


