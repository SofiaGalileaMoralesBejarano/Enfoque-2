# Enfoque 2: Percepción
# Autor: Sofia Galilea Morales Bejarano 6°E

# Objetivo: 
# Carga una imagen en escala de grises, aplica el detector de bordes Canny y muestra tanto la imagen original como la imagen con los bordes detectados.


# Inicio:

import cv2
from matplotlib import pyplot as plt

# Cargar la imagen en escala de grises
imagen = cv2.imread('Soldaditos.JPG', cv2.IMREAD_GRAYSCALE)

if imagen is None:
    # Verificación de que la imagen se cargó correctamente
    print("No se pudo cargar la imagen. Asegúrate de especificar una ruta válida.")
else:
    # Aplicar detector de bordes Canny
    bordes = cv2.Canny(imagen, 100, 200)

    # Crear figura para mostrar imágenes
    plt.figure(figsize=(10, 5))

    # Imagen original
    plt.subplot(1, 2, 1)
    plt.imshow(imagen, cmap='gray')
    plt.title("Imagen Original")
    plt.axis("off")

    # Imagen con bordes detectados
    plt.subplot(1, 2, 2)
    plt.imshow(bordes, cmap='gray')
    plt.title("Detección de Bordes")
    plt.axis("off")

    # Mostrar las imágenes
    plt.show()
