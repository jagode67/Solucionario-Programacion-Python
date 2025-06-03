# Se pide la frase
phrase = input("Enter a phrase: ")
# Se crea un diccionario vacio
char_count = {}

# Se recorre cada uno de los caracteres
for char in phrase:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

# Se imprimen los resultados
print("\nContadar de caracteres:")
for char, count in char_count.items():
    print(f"'{char}': {count} veces")