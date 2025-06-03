import datetime
fecha_str = input("Introduce una fecha (AAAA-MM-DD): ")
fecha = datetime.datetime.strptime(fecha_str, "%Y-%m-%d").date()
hoy = datetime.date.today()
diferencia = (hoy - fecha).days
print("Han pasado", diferencia, "días")
