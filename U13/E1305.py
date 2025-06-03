import matplotlib.pyplot as plt
import numpy as np

# Datos de ejemplo (20 personas)
np.random.seed(42)  # Para reproducibilidad
altura = np.random.normal(170, 10, 20)  # Media 170cm, desviación 10cm
peso = altura * 0.3 + np.random.normal(20, 5, 20)  # Relación aproximada con algo de variación

# Crear el gráfico de dispersión
plt.figure(figsize=(8, 6))
plt.scatter(altura, peso, color='blue', alpha=0.6)

# Personalizar el gráfico
plt.title('Relación entre Altura y Peso')
plt.xlabel('Altura (cm)')
plt.ylabel('Peso (kg)')

# Añadir cuadrícula
plt.grid(True, linestyle='--', alpha=0.7)

# Ajustar los márgenes
plt.tight_layout()

# Mostrar el gráfico
plt.show()