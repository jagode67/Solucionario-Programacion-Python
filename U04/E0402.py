# Request a num from the user
num = int(input("Introducir un número: "))

print(f"Parejas de números cuya suma de {num}:")

for i in range(num + 1):
    for j in range(i, num + 1):
        if i + j == num:
            print(f"{i} + {j} = {num}")