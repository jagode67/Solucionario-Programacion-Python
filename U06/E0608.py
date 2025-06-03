from datetime import datetime

def convertir_fecha(fecha_str):
    fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
    return fecha.strftime("%Y-%m-%d")

print(convertir_fecha("15/04/2023"))  # 2023-04-15
