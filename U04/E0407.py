numbers = []
even_count = 0
odd_count = 0

# Get numbers from user until 0 is entered
while True:
    number = int(input("Introducir un número (0 para finalizar): "))
    if number == 0:
        break
    numbers.append(number)
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

# Display results
print("\nLista de números:", numbers)
print(f"Cantidad de pares: {even_count}")
print(f"Cantidad de impares: {odd_count}")