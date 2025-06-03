cadena = input("Introduce una cadena: ")
indice = cadena.find("a")
while indice != -1:
    print(indice, end=" ")
    indice = cadena.find("a", indice + 1)
