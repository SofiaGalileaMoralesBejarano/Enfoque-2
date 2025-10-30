# Enfoque 2 - Traduccion automatica estadistica
# Autor: Sofia Galilea Morales Bejarano 6°E

# Objetivo:

# El código implementa un traductor automático estadístico básico que traduce palabra por palabra usando un diccionario predefinido español-inglés.
# Cada palabra se busca en el diccionario y, si no existe, se conserva sin traducir.
# Su objetivo es simular el funcionamiento inicial de la traducción automática estadística, 
# donde la traducción se basa en probabilidades o asociaciones directas entre palabras.


# Inicio:

class TraductorEstadistico:
    def __init__(self):
        # Diccionario de traducción simple
        self.diccionario = {
            'hola': 'hello',
            'adios': 'goodbye',
            'gracias': 'thank you',
            'por favor': 'please',
            'si': 'yes',
            'no': 'no'
        }

    def traducir(self, frase):
        """Traduce una frase palabra por palabra usando el diccionario."""
        palabras = frase.split()  # Divide la frase en palabras
        traduccion = []

        for palabra in palabras:
            # Busca la traducción en el diccionario
            traduccion.append(self.diccionario.get(palabra.lower(), palabra))  # Si no hay traducción, mantiene la palabra

        return ' '.join(traduccion)  # Une las palabras traducidas en una frase

traductor = TraductorEstadistico()

frase_original = "hola gracias por favor"
frase_traducida = traductor.traducir(frase_original)

print("Frase original:", frase_original)
print("Frase traducida:", frase_traducida)
