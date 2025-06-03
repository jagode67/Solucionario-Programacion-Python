palabra = input("Introduce una palabra: ")
if palabra == palabra[::-1]:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")
