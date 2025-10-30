# Enfoque 2 - Procesos Estacionarios
# Autor: Sofia galilea Morales Bejarano 6°E

# Objetivo del programa:

# El código genera un proceso estacionario de ruido blanco, es decir, una secuencia de valores aleatorios con media y varianza constantes en el tiempo.
# Usa una distribución normal para crear las muestras y luego grafica su comportamiento temporal.
# Su objetivo es simular y analizar un proceso aleatorio estable, calculando su media y varianza para comprobar la estacionariedad.


# Inicio del programa:
import numpy as np
import matplotlib.pyplot as plt

# Parámetros del proceso estacionario
n_muestras = 1000  # Número de muestras a generar
media = 0          # Media del proceso
desviacion_estandar = 1  # Desviación estándar del proceso

# Generación del proceso de ruido blanco (proceso estacionario)
ruido_blanco = np.random.normal(media, desviacion_estandar, n_muestras)

# Visualización del proceso estacionario
plt.plot(ruido_blanco, color='blue', alpha=0.7, label='Ruido Blanco')
plt.title('Proceso Estacionario - Ruido Blanco')
plt.xlabel('Tiempo')
plt.ylabel('Valor')
plt.grid()
plt.legend()
plt.show()

# Cálculo de la media y la varianza
media_calculada = np.mean(ruido_blanco)
varianza_calculada = np.var(ruido_blanco)

print(f"Media calculada: {media_calculada:.2f}")
print(f"Varianza calculada: {varianza_calculada:.2f}")
