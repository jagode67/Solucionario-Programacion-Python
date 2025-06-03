frase = input("Introduce una frase: ")
for palabra in frase.split():
    if palabra[0].isupper():
        print(palabra)

