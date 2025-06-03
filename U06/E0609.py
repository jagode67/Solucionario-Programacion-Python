def buscar_en_diccionario(diccionario, valor):
    return [k for k, v in diccionario.items() if v == valor]

dic = {'a': 1, 'b': 2, 'c': 1}
print(buscar_en_diccionario(dic, 1))  # ['a', 'c']
