# Enfoque 2: Red Bayesiana
# Autor: Sofia Galilea Morales Bejarano 6°E

# Objetivo:

# Implementa una red bayesiana simple para almacenar y consultar
# probabilidades condicionales entre eventos relacionados.


# Inicio:

from collections import defaultdict       

class RedBayesiana:
    def __init__(self):
        # Diccionario anidado para guardar P(evento | dado_evento)
        self.probabilidades = defaultdict(dict)

    def agregar_probabilidad(self, evento, dado_evento, probabilidad):
        # Agrega una probabilidad condicional a la red
        self.probabilidades[evento][dado_evento] = probabilidad

    def calcular_probabilidad(self, evento, dado_evento):
        # Devuelve P(evento | dado_evento) si está definida
        return self.probabilidades[evento].get(dado_evento, "Probabilidad no definida en la red.")

    def mostrar_probabilidades(self):
        # Muestra todas las probabilidades registradas
        for evento, condicionadas in self.probabilidades.items():
            for dado_evento, probabilidad in condicionadas.items():
                print(f"P({evento} | {dado_evento}) = {probabilidad}")

# Crear instancia de la red bayesiana
red = RedBayesiana()

# Agregar probabilidades a la red
red.agregar_probabilidad('Luna', 'Sofia', 0.75)
red.agregar_probabilidad('Diego', 'Sofia', 0.55)
red.agregar_probabilidad('Sofia', 'Diego', 0.82)

# Consultar probabilidades específicas
prob_luna_dado_sofia = red.calcular_probabilidad('Luna', 'Sofia')
prob_diego_dado_sofia = red.calcular_probabilidad('Diego', 'Sofia')

# Mostrar los resultados
print("\nResultados de la Red Bayesiana:")
print(f"La probabilidad de que ocurra 'Luna' dado que ocurrió 'Sofia' es: {prob_luna_dado_sofia}")
print(f"La probabilidad de que ocurra 'Diego' dado que ocurrió 'Sofia' es: {prob_diego_dado_sofia}")

print("\nProbabilidades en la Red:")
red.mostrar_probabilidades()
