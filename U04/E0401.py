lista = [1, 2, 2, 3, 4, 4, 5, 1]
lista_sin_duplicados = []

for elemento in lista:
    if elemento not in lista_sin_duplicados:
        lista_sin_duplicados.append(elemento)

print(lista_sin_duplicados)  # Salida: [1, 2, 3, 4, 5]
