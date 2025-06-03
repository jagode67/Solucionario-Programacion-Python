import matplotlib.pyplot as plt

# Datos de ejemplo
x = [1, 2, 3, 4, 5]
y = [2, 5, 3, 8, 6]

# Crear una figura de tamaño personalizado
plt.figure(figsize=(10, 6))

# Crear múltiples líneas con diferentes marcadores
plt.plot(x, y, color='blue', marker='s', markersize=10, 
         markerfacecolor='red', markeredgecolor='black', 
         markeredgewidth=2, linestyle='-', label='Cuadrados')

# Añadir una segunda serie con triángulos
y2 = [i + 1 for i in y]
plt.plot(x, y2, color='green', marker='^', markersize=10, 
         markerfacecolor='yellow', markeredgecolor='black', 
         markeredgewidth=2, linestyle='--', label='Triángulos')

# Personalizar el gráfico
plt.title('Gráfico con Marcadores Personalizados')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend()

# Mostrar el gráfico
plt.show()