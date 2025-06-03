def ordenar_lista(lista, reversa=False):
    return sorted(lista, reverse=reversa)

print(ordenar_lista([3,1,4,2], True))  # [4, 3, 2, 1]


