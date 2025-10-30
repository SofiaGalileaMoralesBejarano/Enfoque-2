# Enfoque 2 - Filtrado, Prediccion, Suavizado y Explicacion
# Autor: Sofia Galilea Morales Bejarano 6°E

# Objetivo:
# Compara el estado real, las observaciones ruidosas y el estado filtrado para mostrar cómo se mejora la estimación.
# Su objetivo es reducir el efecto del ruido y obtener una estimación más precisa del comportamiento del sistema en el tiempo.

# Inicio:

import numpy as np
import matplotlib.pyplot as plt

# Parámetros del sistema dinámico
n_pasos = 50
estado_real = np.zeros(n_pasos)
estado_filtrado = np.zeros(n_pasos)
observaciones = np.zeros(n_pasos)

# Configuración de ruido y factores de actualización
ruido_proceso = 0.5
ruido_observacion = 1.0
prediccion_estado = 0.0
prediccion_error = 1.0

# Factor de ganancia
factor_ganancia = prediccion_error / (prediccion_error + ruido_observacion)

# Simulación del sistema dinámico con ruido
for t in range(1, n_pasos):
    # Estado real en el tiempo t (con ruido)
    estado_real[t] = estado_real[t-1] + np.random.normal(0, ruido_proceso)
    # Observación en el tiempo t (con ruido de observación)
    observaciones[t] = estado_real[t] + np.random.normal(0, ruido_observacion)

    # Filtrado: Estimación del estado en t
    estado_filtrado[t] = prediccion_estado + factor_ganancia * (observaciones[t] - prediccion_estado)

    # Predicción: Estado en el siguiente paso
    prediccion_estado = estado_filtrado[t]
    prediccion_error = (1 - factor_ganancia) * prediccion_error + ruido_proceso

plt.plot(estado_real, label="Estado Real", color='green')
plt.plot(observaciones, label="Observaciones", color='red', linestyle='dotted')
plt.plot(estado_filtrado, label="Estado Filtrado", color='blue')
plt.title("Filtrado y Predicción en un Sistema Dinámico")
plt.xlabel("Tiempo")
plt.ylabel("Valor del Estado")
plt.legend()
plt.grid()
plt.show()
