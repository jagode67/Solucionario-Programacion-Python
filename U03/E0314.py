altura = int(input("Introduce la altura del triángulo: "))

for i in range(1, altura + 1):
  print(" " * (altura - i), end="")

  for j in range(1, i + 1):
    print(j, end=" ")

  print()
