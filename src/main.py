from image_prosessor import ImageProsessor
from matrix_operator import MatrixOperations
from utils import show_image, save_image, print_matrix
import time

def main():

    procesador1 = ImageProsessor("images/imagen1.jpg")
    procesador2 = ImageProsessor("images/imagen2.jpg")


    print(f"Tamaño imagen 1: {procesador1.find_size()}")
    print(f"Tamaño imagen 2: {procesador2.find_size()}")

    tamano_cuadrado = min(procesador1.find_size()[0], procesador1.find_size()[1])
    imagen1_crop = procesador1.cut(0, tamano_cuadrado, 0, tamano_cuadrado)
    imagen2_crop = procesador2.cut(0, tamano_cuadrado, 0, tamano_cuadrado)

    show_image(imagen1_crop, "Imagen 1 Recortada")
    show_image(imagen2_crop, "Imagen 2 Recortada")
    save_image(imagen1_crop, "images/imagen1Crop.jpg")
    time.sleep(3)
    objImageCrop = ImageProsessor("images/imagen1Crop.jpg")
    imagen1_gris = objImageCrop.covert_to_gray_scale()


    show_image(imagen1_gris, "Imagen 1 en Escala de Grises")

    img_transpose = objImageCrop.transpose_image()
    show_image(img_transpose, "Imagen 1 en Escala de Grises")
    inversa_imagen1 = MatrixOperations.check_reverse(imagen1_gris)
    if inversa_imagen1 is not None:
        print("La imagen 1 tiene inversa.")
        print_matrix(inversa_imagen1)
    else:
        print("La imagen 1 no tiene inversa.")

    imagen1_alfa_mayor_1 = MatrixOperations.multiply_by_scalar(imagen1_gris, 1.5)  # Contraste aumentado
    show_image(imagen1_alfa_mayor_1, "Imagen con Contraste Aumentado (α > 1)")

    imagen1_alfa_menor_1 = MatrixOperations.multiply_by_scalar(imagen1_gris, 0.5)  # Contraste reducido
    show_image(imagen1_alfa_menor_1, "Imagen con Contraste Reducido (0 < α < 1)")


    imagen1_volteada = MatrixOperations.turn_image_x_axis(imagen1_gris)
    show_image(imagen1_volteada, "Imagen Volteada")

    imagen1_negativa = objImageCrop.calculate_negative()
    show_image(imagen1_negativa, "Imagen Negativa")

if __name__ == "__main__":
    main()