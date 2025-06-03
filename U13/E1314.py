import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Crear datos de ejemplo (matriz de correlación)
np.random.seed(42)
datos = np.random.rand(5, 5)  # Matriz 5x5 de números aleatorios
# Hacer la matriz simétrica para que parezca una matriz de correlación real
datos = (datos + datos.T) / 2
np.fill_diagonal(datos, 1)  # Diagonal principal con 1's

# Nombres de las variables
variables = ['Var A', 'Var B', 'Var C', 'Var D', 'Var E']

# Crear la figura
plt.figure(figsize=(10, 8))

# Crear el mapa de calor
sns.heatmap(datos, 
            annot=True,           # Mostrar valores numéricos
            cmap='coolwarm',      # Esquema de colores
            vmin=-1, vmax=1,      # Rango de valores
            center=0,             # Centro del mapa de calor
            square=True,          # Hacer las celdas cuadradas
            xticklabels=variables,
            yticklabels=variables,
            fmt='.2f')            # Formato de los números (2 decimales)

# Añadir título
plt.title('Matriz de Correlación')

# Ajustar los márgenes
plt.tight_layout()

# Mostrar el gráfico
plt.show()