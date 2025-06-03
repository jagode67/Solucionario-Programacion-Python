import matplotlib.pyplot as plt

# Datos de la encuesta (ejemplo)
categorias = ['Muy satisfecho', 'Satisfecho', 'Neutral', 'Insatisfecho', 'Muy insatisfecho']
valores = [45, 30, 15, 7, 3]  # Porcentajes

# Crear la figura
plt.figure(figsize=(10, 8))

# Crear el gráfico de sectores
plt.pie(valores, 
        labels=categorias,
        autopct='%1.1f%%',  # Mostrar porcentajes con un decimal
        startangle=90,      # Empezar desde arriba
        colors=['#2ecc71', '#3498db', '#95a5a6', '#e74c3c', '#c0392b'],
        explode=(0.1, 0, 0, 0, 0))  # Destacar el primer sector

# Añadir título
plt.title('Resultados de la Encuesta de Satisfacción')

# Asegurar que el círculo sea proporcional
plt.axis('equal')

# Añadir leyenda
plt.legend(categorias, title="Niveles de Satisfacción", 
          loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Ajustar los márgenes para que quepa la leyenda
plt.tight_layout()

# Mostrar el gráfico
plt.show()