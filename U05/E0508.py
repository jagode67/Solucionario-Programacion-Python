mayor = ""
while True:
    cad = input("Introduce una cadena (fin para terminar): ")
    if cad == "fin":
        break
    if len(cad) > len(mayor):
        mayor = cad
print("La cadena más larga es:", mayor)
