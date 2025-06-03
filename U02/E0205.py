numero = int(input("Introduce un número: "))
esta_en_rango = numero >= 0 and numero <= 100
# Alternativa: esta_en_rango = 0 <= numero <= 100
print(f"¿El número {numero} está entre 0 y 100? {esta_en_rango}")