def elemento_mas_frecuente(lista):
    conteo = {}
    for elem in lista:
        if elem in conteo:
            conteo[elem] += 1
        else:
            conteo[elem] = 1
    max_elem = max(conteo, key=conteo.get)
    return (max_elem, conteo[max_elem])

print(elemento_mas_frecuente([1, 2, 2, 3, 3, 3, 4, 2, 3]))  # (3, 4)
print(elemento_mas_frecuente(["a", "b", "a", "c", "a", "b"]))  # ('a', 3)
