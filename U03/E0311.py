lado = int(input("Tamaño del cuadrado: "))

# Crear el cuadrado hueco
for i in range(lado):
    for j in range(lado):
        # Pinta * en la primera línea, última línea, primera columna y última columna
        if i == 0 or i == lado - 1 or j == 0 or j == lado - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()  # Nueva línea