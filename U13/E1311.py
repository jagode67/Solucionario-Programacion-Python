import matplotlib.pyplot as plt
import numpy as np

# Crear datos de ejemplo
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)

# Crear una figura con tres subgráficos
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 12))

# Primer subgráfico: Seno
ax1.plot(x, y1, 'b-', label='Seno')
ax1.set_title('Función Seno')
ax1.set_xlabel('x')
ax1.set_ylabel('sin(x)')
ax1.grid(True)
ax1.legend(loc='upper right', fontsize=12, bbox_to_anchor=(1.15, 1))

# Segundo subgráfico: Coseno
ax2.plot(x, y2, 'r--', label='Coseno')
ax2.set_title('Función Coseno')
ax2.set_xlabel('x')
ax2.set_ylabel('cos(x)')
ax2.grid(True)
ax2.legend(loc='center left', fontsize=12, bbox_to_anchor=(1.15, 0.5))

# Tercer subgráfico: Tangente
ax3.plot(x, y3, 'g:', label='Tangente')
ax3.set_title('Función Tangente')
ax3.set_xlabel('x')
ax3.set_ylabel('tan(x)')
ax3.grid(True)
ax3.legend(loc='lower right', fontsize=12, bbox_to_anchor=(1.15, 0))

# Ajustar el espaciado entre subgráficos
plt.tight_layout()

# Mostrar la figura
plt.show()