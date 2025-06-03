import matplotlib.pyplot as plt

# Datos de ejemplo
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

# Crear el gráfico
plt.plot(x, y)  # Línea con marcadores circulares

# Personalizar el gráfico
plt.title('Gráfico de Línea Simple')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')

# Mostrar el gráfico
plt.show()