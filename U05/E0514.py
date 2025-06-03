import datetime
fecha_str = input("Introduce una fecha (AAAA-MM-DD): ")
fecha = datetime.datetime.strptime(fecha_str, "%Y-%m-%d")
hoy = datetime.datetime.today()
if fecha < hoy:
    print("Es anterior a hoy")
elif fecha > hoy:
    print("Es posterior a hoy")
else:
    print("Es hoy")

