phrase = input("Introducir una frase: ")

# Define vocales (including both lowercase and uppercase)
vocales = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
#Iniciliza el contador
cuenta = 0
# Busca las vocales en la lista
for character in phrase:
    if character in vocales:
        cuenta += 1
# Muestra el resultado
print(f"La frase contiene {cuenta} vocales")