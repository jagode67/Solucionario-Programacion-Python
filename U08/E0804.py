import math

def raiz_cuadrada(numero):
    try:
        assert numero >= 0, "No se puede calcular la raíz cuadrada de un número negativo"
        return math.sqrt(numero)
    except AssertionError as e:
        return f"Error: {e}"

# Pruebas
print(raiz_cuadrada(16))  # 4.0
print(raiz_cuadrada(-4))  # Error: No se puede calcular la raíz cuadrada de un número negativo