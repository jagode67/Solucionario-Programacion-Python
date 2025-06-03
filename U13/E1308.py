import matplotlib.pyplot as plt
import numpy as np

# Generar datos de ejemplo
x = np.linspace(0, 10, 10)
y1 = np.sin(x)
y2 = np.cos(x)

# Crear una figura de tamaño personalizado
plt.figure(figsize=(10, 6))

# Crear dos líneas con diferentes estilos
plt.plot(x, y1, linestyle='--', marker='o', color='blue', 
         markersize=8, linewidth=2)
plt.plot(x, y2, linestyle=':', marker='o', color='red',
         markersize=8, linewidth=2)

# Personalizar el gráfico
plt.title('Gráfico con Líneas Discontinuas y Marcadores')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.grid(True, linestyle='-', alpha=0.3)

# Ajustar los márgenes
plt.tight_layout()

# Mostrar el gráfico
plt.show()