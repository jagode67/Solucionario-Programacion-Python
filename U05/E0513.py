frase = input("Introduce una frase: ")
for palabra in frase.split():
    if "a" in palabra:
        print(palabra)
