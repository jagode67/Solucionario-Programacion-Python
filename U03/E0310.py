lado = int(input("Tamaño del cuadrado: "))

# Con 2 for
for i in range(lado):
    for j in range(lado):
        print("*", end="")
    print()  #
print("."*10)
# Con 1 for
for i in range(lado):
    print("*"*lado)
