def estadisticas_texto(texto):
    palabras = texto.split()
    return {
        'palabras': len(palabras),
        'caracteres': len(texto),
        'promedio': len(texto)/len(palabras) if palabras else 0
    }

print(estadisticas_texto("Hola mundo Python"))  # {'palabras': 3, ...}
