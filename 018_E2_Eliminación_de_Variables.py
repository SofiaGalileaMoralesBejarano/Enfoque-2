# Enfoque 2 - Eliminacion de variables
# Autor: Sofia Galilea Morales Bejarano 6°E

# Objetivo: 

#El código implementa una red bayesiana simplificada que permite calcular probabilidades condicionales entre eventos.
# Su objetivo es simular el proceso de inferencia probabilística mediante la combinación de probabilidades condicionales almacenadas.


# Inicio del programa:
from collections import defaultdict       # importa defaultdict, una estructura de diccionario con valores por defecto

class RedBayesiana:                       # define una clase llamada RedBayesiana
    def __init__(self):                   # método constructor de la clase
        self.probabilidades = defaultdict(dict)   # crea un diccionario anidado para guardar las probabilidades condicionales

    def agregar_probabilidad(self, evento, dado_evento, probabilidad):
        # agrega una probabilidad condicional del tipo P(evento | dado_evento)
        self.probabilidades[evento][dado_evento] = probabilidad

    def eliminar_variable(self, evento_objetivo, evidencia, variables_a_eliminar):
        # simula el proceso de eliminación de variables para calcular P(evento_objetivo | evidencia)
        probabilidad_total = 0.0          # inicializa acumulador para la probabilidad total
        
        for valor in variables_a_eliminar:          # recorre las variables que se eliminarán
            probabilidad = self.calcular_probabilidad(evento_objetivo, evidencia, valor)
            # calcula la contribución de cada variable a eliminar
            probabilidad_total += probabilidad      # suma las probabilidades parciales
        
        return probabilidad_total         # devuelve la probabilidad total resultante

    def calcular_probabilidad(self, evento, evidencia, variable):
        # calcula P(evento | variable) * P(evidencia | variable)
        if variable in self.probabilidades[evento]:      # verifica si la probabilidad está registrada
            return self.probabilidades[evento][variable] * self.probabilidades[evidencia][variable]
        else:
            return 0.0                                   # devuelve 0 si no existe esa relación en la red

# Crear una instancia de la Red Bayesiana
red = RedBayesiana()                       # crea un objeto de tipo RedBayesiana

# Agregar probabilidades a la red
red.agregar_probabilidad('A', 'B', 0.9)    # define P(A | B) = 0.9
red.agregar_probabilidad('A', '¬B', 0.2)   # define P(A | ¬B) = 0.2
red.agregar_probabilidad('B', 'C', 0.7)    # define P(B | C) = 0.7
red.agregar_probabilidad('B', '¬C', 0.4)   # define P(B | ¬C) = 0.4

# Calcular P(A | B) eliminando la variable 'C'
variables_a_eliminar = ['C']               # se decide eliminar la variable oculta C
probabilidad_A_dado_B = red.eliminar_variable('A', 'B', variables_a_eliminar)
# llama al método que suma las probabilidades de P(A | B, C) * P(B | C) (aproximado aquí)

print(f"La probabilidad P(A | B) usando eliminación de variables es: {probabilidad_A_dado_B:.4f}")
# muestra el resultado formateado con 4 decimales
