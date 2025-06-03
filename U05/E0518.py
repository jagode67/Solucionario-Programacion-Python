import datetime
fecha_str = input("Introduce una fecha (AAAA-MM-DD): ")
fecha = datetime.datetime.strptime(fecha_str, "%Y-%m-%d").date()
if fecha.weekday() >= 5:
    print("Es fin de semana")
else:
    print("Es día laborable")
