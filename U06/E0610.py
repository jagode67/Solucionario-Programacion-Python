import math

def calculadora_cientifica(funcion, valor):
    funciones = {
        'seno': math.sin,
        'coseno': math.cos,
        'raiz': math.sqrt
    }
    return funciones.get(funcion, lambda x: "Función no válida")(valor)

print(calculadora_cientifica('raiz', 16))  # 4.0

