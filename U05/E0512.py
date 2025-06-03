frase = input("Introduce una frase: ")
contador = 0
for palabra in frase.split():
    if palabra.isdigit():
        contador += 1
print("Números encontrados:", contador)
