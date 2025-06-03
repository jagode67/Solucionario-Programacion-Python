import matplotlib.pyplot as plt
import numpy as np

# Generar datos aleatorios
np.random.seed(42)  # Para reproducibilidad
datos = np.random.normal(loc=100, scale=15, size=1000)  # Media=100, Desviación=15

# Crear la figura
#plt.figure(figsize=(10, 6))

# Crear el histograma
plt.hist(datos, bins=30, color='skyblue', edgecolor='black', alpha=0.7)

# Personalizar el gráfico
plt.title('Histograma de Números Aleatorios')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')

# Mostrar el gráfico
plt.show()