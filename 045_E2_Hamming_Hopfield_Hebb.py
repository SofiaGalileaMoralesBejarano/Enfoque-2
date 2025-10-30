# Enfoque 2 - Hamming, Hopfield, Hebb, Boltzmann
# Autor: Sofia Galilea Morales Bejarano 6°E

# Objetivo:

# Implementa una red de Hopfield como memoria asociativa: aprende patrones binarios con una regla tipo hebbiana (matriz de pesos y sin autoconexión).
# Dado un patrón ruidoso, la dinámica iterativa lo corrige actualizando neuronas y converge a un atractor (patrón almacenado).
# Calcula la energía del estado para mostrar cómo la red busca mínimos durante el recuerdo.


# Inicio del programa: 

import numpy as np
import matplotlib.pyplot as plt

class HopfieldNetwork:
    def __init__(self, size):
        self.size = size
        self.weights = np.zeros((size, size))

    def train(self, patterns):
        """Entrena la red con patrones dados."""
        for p in patterns:
            p = p.reshape(self.size, 1)
            self.weights += np.dot(p, p.T)
        # Eliminamos la auto-conexión
        np.fill_diagonal(self.weights, 0)

    def recall(self, pattern, steps=5):
        """Recuerda un patrón dado a través de la red."""
        state = pattern.copy()
        for _ in range(steps):
            for i in range(self.size):
                net_input = np.dot(self.weights[i], state)
                state[i] = 1 if net_input > 0 else -1  # Aplicar función de activación
        return state

    def energy(self, state):
        """Calcula la energía del estado actual."""
        return -0.5 * np.dot(state.T, np.dot(self.weights, state))

# Definimos algunos patrones de ejemplo
patterns = np.array([[1, 1, -1, -1], 
                     [-1, -1, 1, 1], 
                     [1, -1, 1, -1]])

# Creamos la red de Hopfield
hopfield_net = HopfieldNetwork(size=4)

# Entrenamos la red
hopfield_net.train(patterns)

# Probamos recordar un patrón perturbado
test_pattern = np.array([1, -1, -1, -1])  # Patrón perturbado
recalled_pattern = hopfield_net.recall(test_pattern)

# Mostramos los resultados
print("Patrón de prueba:", test_pattern)
print("Patrón recordado:", recalled_pattern)

# Visualizamos la energía del patrón original y del recordado
original_energy = hopfield_net.energy(test_pattern)
recalled_energy = hopfield_net.energy(recalled_pattern)

print("Energía del patrón original:", original_energy)
print("Energía del patrón recordado:", recalled_energy)
