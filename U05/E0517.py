import datetime
f1 = input("Introduce la primera fecha (DD-MM-AAA): ")
f2 = input("Introduce la segunda fecha (DD-MM-AAAA): ")
fecha1 = datetime.datetime.strptime(f1, "%d-%m-%Y").date()
fecha2 = datetime.datetime.strptime(f2, "%d-%m-%Y").date()
if fecha1 > fecha2:
    print("La primera fecha es la más reciente")
elif fecha2 > fecha1:
    print("La segunda fecha es la más reciente")
else:
    print("Ambas fechas son iguales")
