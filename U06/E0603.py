def contar_vocales(texto):
    return sum(1 for letra in texto.lower() if letra in 'aeiouáéíóú')

print(contar_vocales("Hola Mundo"))  # 4
