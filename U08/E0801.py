try:
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    resultado = num1 / num2
    print(f"El resultado de {num1} / {num2} = {resultado}")
except ZeroDivisionError:
    print("¡Error! No se puede dividir entre cero.")
except ValueError:
    print("¡Error! Introduce un valor numérico válido.")
finally:
    print("Operación finalizada.")