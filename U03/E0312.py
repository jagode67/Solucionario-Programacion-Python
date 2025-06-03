# Get input from user
num = int(input("Introduce un número: "))

print(f"Números primos menores que {num}:")
for num in range(2, num + 1):
    es_primo = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            es_primo = False
            break
    if es_primo:
        print(num, end=" ")
