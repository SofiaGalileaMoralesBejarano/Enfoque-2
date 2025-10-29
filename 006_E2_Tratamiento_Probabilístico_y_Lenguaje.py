# Enfoque 2: Tratamiento Probabilístico y Lenguaje
# Autor: Sofia Galilea Morales Bejranano 6°E

# Objetivo:
# Analiza un corpus de noticias con NLTK, calcula frecuencias de palabras y bigramas, y predice las palabras más probables que siguen a una dada.


# Inicio:

import nltk
from nltk.corpus import brown
from nltk.probability import FreqDist, ConditionalFreqDist

# Descargar corpus y tokenizador si no están disponibles
nltk.download("brown")
nltk.download("punkt")

# Seleccionamos las palabras del corpus 'news'
corpus = brown.words(categories='news')  

# Frecuencia simple de palabras en el corpus
fdist = FreqDist(corpus)
print("10 palabras más comunes en el corpus:")
for palabra, frecuencia in fdist.most_common(10):
    print(f"{palabra}: {frecuencia}")

# Creación de bigramas (pares de palabras consecutivas)
bigrams = nltk.bigrams(corpus)

# Distribución condicional de frecuencias: P(palabra_siguiente | palabra_actual)
cfd = ConditionalFreqDist(bigrams)

def predecir_siguiente(palabra_actual, num=3):
    """
    Predice las palabras más probables que siguen a 'palabra_actual'
    usando la distribución condicional de bigramas.
    """
    palabra_actual = palabra_actual.lower()
    if palabra_actual in cfd:
        palabras_probables = cfd[palabra_actual].most_common(num)
        print(f"Palabras más probables después de '{palabra_actual}':")
        for palabra, frecuencia in palabras_probables:
            print(f"  {palabra}: {frecuencia}")
    else:
        print(f"No se encontraron predicciones para la palabra '{palabra_actual}'.")

# Ejemplo de predicción
predecir_siguiente("the")
