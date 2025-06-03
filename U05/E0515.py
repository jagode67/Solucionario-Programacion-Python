cadena = input("Introduce una cadena: ")
for caracter in set(cadena):
    print(f"{caracter}: {cadena.count(caracter)}")


