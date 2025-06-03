import math

# Get coefficients
print("Introducir los coheficientes para ax² + bx + c = 0")
a = float(input("Introducir a: "))
b = float(input("Introducir b: "))
c = float(input("Introducir c: "))

# Comprobación de los coeficientes
if a == 0:
    if b == 0:
        if c == 0:
            print("Infinitas soluciones (0 = 0)")
        else:
            print("Sin solución (ecuación imposible)")
    else:
        x = -c / b
        print(f"Solución: x = {x}")
else:
    # Calcular discriminantee
    discriminante = b**2 - 4*a*c
    
    if discriminante > 0:
        # dos soluciones reales
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        print(f"Dos soluciones:")
        print(f"x1 = {x1}")
        print(f"x2 = {x2}")
    elif discriminante == 0:
        # Una solución real
        x = -b / (2*a)
        print(f"Una solución: x = {x}")
    else:
        print(f"No tiene solución real")
