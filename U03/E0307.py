num = int(input("Introduce un número: "))
total = 0

print(f"Sumando números desde 1 a {num}:")
for i in range(1, num + 1):
    total += i
    print(f"{i} -> Subtotal: {total}")

print(f"\nSuma final: {total}")