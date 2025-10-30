# Enfoque 2 - Inferencia por enumeracion
# Autor: Sofia Galilea Morales Bejarano 6°E

# Objetivo: 
# El código crea una red bayesiana para representar relaciones probabilísticas entre eventos.
# Permite agregar y calcular probabilidades condicionales como 𝑃 (𝐴∣𝐵) P (A∣B) usando inferencia por enumeración.
# Su objetivo es inferir la probabilidad de un evento dado otro aplicando las reglas de la probabilidad total.

# Inicio:
from collections import defaultdict

class RedBayesiana:
    def __init__(self):
        # Usamos un diccionario para almacenar las probabilidades condicionales
        self.probabilidades = defaultdict(dict)
    
    # Método para agregar las probabilidades condicionales a la red
    def agregar_probabilidad(self, evento, dado_evento, probabilidad):
        """
        Agrega P(evento | dado_evento) a la red bayesiana.
        """
        self.probabilidades[evento][dado_evento] = probabilidad

    # Método para calcular la probabilidad total usando inferencia por enumeración
    def inferencia_por_enumeracion(self, evento_objetivo, dado_evento, valores_dado_evento):
        """
        Calcula P(evento_objetivo | dado_evento) usando inferencia por enumeración.
        """
        probabilidad_total = 0.0
        for valor in valores_dado_evento:
            probabilidad = self.calcular_probabilidad(evento_objetivo, valor)
            probabilidad_total += probabilidad * self.calcular_probabilidad(dado_evento, valor)
        
        return probabilidad_total

    def calcular_probabilidad(self, evento, dado_evento):
        """
        Calcula P(evento | dado_evento) si la tenemos en la red.
        """
        if dado_evento in self.probabilidades[evento]:
            return self.probabilidades[evento][dado_evento]
        else:
            return 0.0

# Crear una instancia de la Red Bayesiana
red = RedBayesiana()

# Agregar probabilidades a la red.
red.agregar_probabilidad('A', 'B', 0.9)  # P(A | B)
red.agregar_probabilidad('A', '¬B', 0.2) # P(A | ¬B)
red.agregar_probabilidad('B', 'C', 0.7)  # P(B | C)
red.agregar_probabilidad('B', '¬C', 0.4) # P(B | ¬C)

# Calcular P(A | B)
valores_dado_evento = ['B', '¬B']
probabilidad_A_dado_B = red.inferencia_por_enumeracion('A', 'B', valores_dado_evento)

print(f"La probabilidad P(A | B) es: {probabilidad_A_dado_B:.4f}")
