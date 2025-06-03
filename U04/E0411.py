numbers = []

# Pedir números
while True:
    num = float(input("Introducir números (0 para finalizar): "))
    if num == 0:
        break
    numbers.append(num)

if numbers:
    # Ordenar números
    numbers.sort()
    
    # Calcular mediana
    n = len(numbers)
    if n % 2 == 0:
        # Si hay un número par de elementos, la medina es la media de los dos centrales
        median = (numbers[n//2 - 1] + numbers[n//2]) / 2
    else:
        # Si hay un número impar de elementos, se obtiene el valor del central
        median = numbers[n//2]
    
    # Muestra resultados
    print("\nNúmeros ordenados:", numbers)
    print(f"Mediana: {median}")
else:
    print("No se han introducido números.")