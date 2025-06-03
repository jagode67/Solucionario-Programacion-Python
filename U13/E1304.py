import matplotlib.pyplot as plt

# Datos de ventas mensuales (ejemplo)
meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
ventas = [15000, 18000, 14500, 17000, 19500, 21000, 20000, 22000, 24000, 23000, 20500, 25000]

# Crear el gráfico de barras
plt.figure(figsize=(10, 6))  # Tamaño de la figura
plt.bar(meses, ventas, color='skyblue')  # Crear barras

# Personalizar el gráfico
plt.title('Ventas Mensuales de la Tienda')
plt.xlabel('Meses')
plt.ylabel('Ventas (€)')

# Rotar las etiquetas del eje x para mejor legibilidad
plt.xticks(rotation=45)

# Añadir una cuadrícula para mejor lectura
plt.grid(True, axis='y', linestyle='--', alpha=0.7)

# Mostrar el gráfico
plt.show()