def procesar_lista(lista):
    return {
        'suma': sum(lista),
        'max': max(lista),
        'min': min(lista),
        'promedio': sum(lista)/len(lista)
    }

print(procesar_lista([2,4,6,8]))
