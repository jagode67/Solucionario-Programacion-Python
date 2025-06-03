def operar(a, b, operacion):
    if operacion == "suma":
        return a + b
    elif operacion == "resta":
        return a - b
    else:
        return "Operación no válida"

print(operar(5, 3, "suma"))  # 8
print(operar(10, 4, "resta"))  # 6
print(operar(2, 3, "multiplicacion"))  # Operación no válida
