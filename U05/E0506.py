frase = input("Introduce una frase: ").lower()
for vocal in "aeiou":
    print(f"{vocal}: {frase.count(vocal)}")
