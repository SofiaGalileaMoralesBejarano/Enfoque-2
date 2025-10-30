# Enfoque 2 - Graficos por computador
# Autor: Sofia Galilea Morales Bejarano 6°E

# Objetivo:

# El código genera datos aleatorios y los representa en un gráfico de dispersión donde cada punto tiene color y tamaño distintos.
# Utiliza matplotlib para mostrar cómo los valores varían en dos dimensiones.
# Su objetivo es visualizar patrones o distribuciones en datos de manera clara y atractiva.


# Inicio:

import numpy as np
import matplotlib.pyplot as plt

# Generar datos aleatorios
np.random.seed(0)
n = 100  # Número de puntos
x = np.random.rand(n) * 100  # Coordenadas x
y = np.random.rand(n) * 100  # Coordenadas y
colores = np.random.rand(n)  # Colores aleatorios para cada punto
tamanos = np.random.rand(n) * 100  # Tamaños aleatorios para cada punto

# Crear el gráfico de dispersión
plt.figure(figsize=(10, 6))
plt.scatter(x, y, c=colores, s=tamanos, alpha=0.5, cmap='viridis')

# Etiquetas y título
plt.title('Gráfico de Dispersión de Datos Aleatorios', fontsize=16)
plt.xlabel('Eje X', fontsize=14)
plt.ylabel('Eje Y', fontsize=14)
plt.grid(True)

plt.colorbar(label='Colores')
plt.show()
