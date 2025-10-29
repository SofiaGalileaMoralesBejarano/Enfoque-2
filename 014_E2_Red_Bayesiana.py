# Enfoque 2- Red Bayesiana
# Autor: Sofia Galilea Morales Bejarano 6°E

# Objetivo:
# Guardar y consultar probabilidades condicionales en una red bayesiana simple, y mostrarlas.

# Inicio de programa: 
from collections import defaultdict
from typing import Dict, Iterable, Tuple, Union

class RedBayesiana:
    def __init__(self):
        # Probabilidades condicionales: P(evento | dado_evento)
        self.probabilidades: Dict[str, Dict[str, float]] = defaultdict(dict)

    def _validar_prob(self, p: float):
        if not (0.0 <= p <= 1.0):
            raise ValueError(f"La probabilidad debe estar en [0,1]. Recibido: {p}")

    def agregar_probabilidad(self, evento: str, dado_evento: str, probabilidad: float) -> None:
        """Agrega/actualiza P(evento | dado_evento)."""
        self._validar_prob(probabilidad)
        self.probabilidades[evento][dado_evento] = probabilidad

    def agregar_probabilidades(self, pares: Iterable[Tuple[str, str, float]]) -> None:
        """Carga en bloque: lista de (evento, dado_evento, probabilidad)."""
        for evento, dado_evento, p in pares:
            self.agregar_probabilidad(evento, dado_evento, p)

    def calcular_probabilidad(self, evento: str, dado_evento: str) -> Union[float, str]:
        """Devuelve P(evento | dado_evento) si existe; si no, mensaje informativo."""
        return self.probabilidades[evento].get(dado_evento, "Probabilidad no definida en la red.")

    def mostrar_probabilidades(self) -> None:
        """Imprime todas las probabilidades ordenadas alfabéticamente."""
        for evento in sorted(self.probabilidades.keys()):
            condicionadas = self.probabilidades[evento]
            for dado_evento in sorted(condicionadas.keys()):
                p = condicionadas[dado_evento]
                print(f"P({evento} | {dado_evento}) = {p:.3f}")

# --- Demostración (misma funcionalidad) ---
red = RedBayesiana()

# Puedes mantener tus nombres originales, o usar otros:
red.agregar_probabilidades([
    ("Mariana", "Sofia", 0.70),
    ("Andrés",  "Sofia", 0.60),
    ("Sofia",   "Andrés", 0.80),
])

# Consultas
prob_mariana_dado_sofia = red.calcular_probabilidad("Mariana", "Sofia")
prob_andres_dado_sofia  = red.calcular_probabilidad("Andrés", "Sofia")

print("\nResultados de la Red Bayesiana:")
print(f"La probabilidad de 'Mariana' dado 'Sofia' es: {prob_mariana_dado_sofia}")
print(f"La probabilidad de 'Andrés' dado 'Sofia' es: {prob_andres_dado_sofia}")

print("\nProbabilidades en la Red:")
red.mostrar_probabilidades()

