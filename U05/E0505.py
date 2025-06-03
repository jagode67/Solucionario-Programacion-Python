cadena = input("Introduce una cadena: ")
letras = digitos = otros = 0
for c in cadena:
    if c.isalpha():
        letras += 1
    elif c.isdigit():
        digitos += 1
    else:
        otros += 1
print("Letras:", letras, "Dígitos:", digitos, "Otros:", otros)
