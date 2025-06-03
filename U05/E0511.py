frase = input("Introduce una frase: ").lower()
contador = 0
for palabra in frase.split():
    if palabra[0] in "aeiou":
        contador += 1
print("Palabras que empiezan por vocal:", contador)
