def obtener_elemento(lista, indice):
    try:
        return lista[indice]
    except IndexError:
        return "Error: Índice fuera de rango."
    except TypeError:
        return "Error: El índice debe ser un entero."
    except Exception as e:
        return f"Error inesperado: {e}"

# Ejemplo de uso
print(obtener_elemento([1, 2, 3], 1))  # 2
print(obtener_elemento([1, 2, 3], 5))  # Error: Índice fuera de rango
print(obtener_elemento([1, 2, 3], "a"))  # Error: El índice debe ser un entero