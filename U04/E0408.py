words = []

# Se piden palabras hasta que se introduce "fin"
while True:
    word = input("Introducir una palabra (fin para acabar): ")
    if word.lower() == "fin":
        break
    words.append(word)

# Orden alfabético
sorted_words = sorted(words, key=str.lower)

# Encuentra la mas larga
longest_word = max(words, key=len) if words else ""

# Muestra resultado
print("\nPalabras en orden alfabético:")
for word in sorted_words:
    print(word)

print(f"\nLa palabra mas larga: {longest_word} ({len(longest_word)} caracteres)")