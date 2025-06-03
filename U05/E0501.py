texto = input("Introduce un texto: ")
contador = 0
for letra in texto:
    if letra.isupper():
        contador += 1
print("Hay", contador, "letras mayúsculas")
