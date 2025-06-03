import matplotlib.pyplot as plt
import numpy as np

# Crear datos para la función seno
x = np.linspace(-2*np.pi, 2*np.pi, 200)  # Valores de x desde -2π hasta 2π
y = np.sin(x)  # Calcular el seno de x

# Crear la figura con alta resolución
plt.figure(figsize=(10, 6), dpi=300)  # dpi=300 para alta resolución

# Dibujar la función seno
plt.plot(x, y, 'b-', label='sin(x)', linewidth=2)

# Añadir una línea horizontal en y=0
plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)

# Añadir una línea vertical en x=0
plt.axvline(x=0, color='k', linestyle='-', alpha=0.3)

# Personalizar el gráfico
plt.title('Función Seno')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.grid(True, alpha=0.3)
plt.legend()

# Establecer límites del eje y
plt.ylim(-1.5, 1.5)

# Ajustar los márgenes
plt.tight_layout()

# Guardar la figura en alta resolución
plt.savefig('seno.png', dpi=300, bbox_inches='tight')

# Mostrar el gráfico
plt.show()