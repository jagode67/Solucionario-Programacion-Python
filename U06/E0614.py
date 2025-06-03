from datetime import datetime, timedelta

def calcular_dias(fecha_inicio, dias):
    fecha = datetime.strptime(fecha_inicio, "%d/%m/%Y")
    return (fecha + timedelta(days=dias)).strftime("%d/%m/%Y")

print(calcular_dias("01/01/2023", 100))  # 11/04/2023
