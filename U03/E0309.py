# Introducir los valores
num1 = int(input("Primer número: "))
num2 = int(input("Segundo número: "))

# Determinar el rango
ini = min(num1, num2)
fin = max(num1, num2)

# Calcular la suma
total = 0
for num in range(ini, fin + 1):
    if num % 2 == 0:
        total += num

print(f"La suma de pares entre {ini} y {fin} es: {total}")