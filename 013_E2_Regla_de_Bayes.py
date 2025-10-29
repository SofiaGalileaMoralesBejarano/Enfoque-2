# Enfoque 2 - Regla de Bayes
# Autor: Sofia Galilea Morales Bejarano 6°E

# Objetivo: El objetivo de este código es aplicar la regla de Bayes para calcular la probabilidad de tener una enfermedad dado un resultado positivo en una prueba médica, 
usando las probabilidades previas y condicionales del problema.


# Inicio de programa:

# Definir las probabilidades
P_enfermedad = 0.01  # Probabilidad de tener la enfermedad (P(E))
P_prueba_pos = 0.9  # Probabilidad de un resultado positivo dado que el paciente tiene la enfermedad (P(P | E))
P_prueba_neg = 0.8  # Probabilidad de un resultado negativo dado que el paciente no tiene la enfermedad (P(N | ¬E))

# Probabilidad de no tener la enfermedad
P_no_enfermedad = 1 - P_enfermedad  # P(¬E)

# Probabilidad de obtener un resultado positivo
P_prueba_pos_total = (P_prueba_pos * P_enfermedad) + (1 - P_prueba_neg) * P_no_enfermedad  # P(P)

# Aplicar la regla de Bayes
P_enfermedad_dado_prueba_pos = (P_prueba_pos * P_enfermedad) / P_prueba_pos_total

print(f"La probabilidad de tener la enfermedad dado un resultado positivo en la prueba es: {P_enfermedad_dado_prueba_pos:.2f}")
