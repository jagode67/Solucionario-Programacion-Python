import string

def contar_palabras(texto):
    texto = texto.lower()
    for signo in string.punctuation:
        texto = texto.replace(signo, "")
    palabras = texto.split()
    frecuencia = {}
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    return frecuencia

print(contar_palabras("Hola mundo, hola Python. Mundo mundo!"))
# {'hola': 2, 'mundo': 3, 'python': 1}
