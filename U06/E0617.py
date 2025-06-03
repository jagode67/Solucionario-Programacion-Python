def conversor_unidades(valor, unidad_origen, unidad_destino):
    factores = {
        ('km', 'mi'): 0.621371,
        ('kg', 'lb'): 2.20462,
        ('°C', '°F'): lambda c: c * 9/5 + 32
    }
    clave = (unidad_origen, unidad_destino)
    if clave in factores:
        return factores[clave](valor) if callable(factores[clave]) else valor * factores[clave]
    return "Conversión no soportada"

print(conversor_unidades(100, 'km', 'mi'))  # 62.1371
print(conversor_unidades(50, 'kg','lb'))  # 110.231
print(conversor_unidades(0, '°C','°F'))  # 32.0
print(conversor_unidades(100, 'km','km'))  # Conversión no soportada