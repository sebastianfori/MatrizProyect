from image_prosessor import ProcesadorImagen
from matrix_operator import OperacionesMatrices
from utils import mostrar_imagen, guardar_imagen

def main():

    procesador1 = ProcesadorImagen("images/imagen1.jpg")
    procesador2 = ProcesadorImagen("images/imagen2.jpg")


    print(f"Tamaño imagen 1: {procesador1.obtener_tamanio()}")
    print(f"Tamaño imagen 2: {procesador2.obtener_tamanio()}")

    tamano_cuadrado = min(procesador1.obtener_tamanio()[0], procesador1.obtener_tamanio()[1])
    imagen1_crop = procesador1.recortar(0, tamano_cuadrado, 0, tamano_cuadrado)
    imagen2_crop = procesador2.recortar(0, tamano_cuadrado, 0, tamano_cuadrado)

    mostrar_imagen(imagen1_crop, "Imagen 1 Recortada")
    mostrar_imagen(imagen2_crop, "Imagen 2 Recortada")

    imagen1_gris = procesador1.convertir_a_grises()
    imagen2_gris = procesador2.convertir_a_grises()

    mostrar_imagen(imagen1_gris, "Imagen 1 en Escala de Grises")
    mostrar_imagen(imagen2_gris, "Imagen 2 en Escala de Grises")


    inversa_imagen1 = OperacionesMatrices.verificar_inversa(imagen1_gris)
    if inversa_imagen1 is not None:
        print("La imagen 1 tiene inversa.")
    else:
        print("La imagen 1 no tiene inversa.")

    imagen1_alfa_mayor_1 = OperacionesMatrices.multiplicar_por_escalar(imagen1_gris, 1.5)  # Contraste aumentado
    mostrar_imagen(imagen1_alfa_mayor_1, "Imagen con Contraste Aumentado (α > 1)")

    imagen1_alfa_menor_1 = OperacionesMatrices.multiplicar_por_escalar(imagen1_gris, 0.5)  # Contraste reducido
    mostrar_imagen(imagen1_alfa_menor_1, "Imagen con Contraste Reducido (0 < α < 1)")


    imagen1_volteada = OperacionesMatrices.voltear_imagen_eje_x(imagen1_gris)
    mostrar_imagen(imagen1_volteada, "Imagen Volteada")

    imagen1_negativa = procesador1.calcular_negativo()
    mostrar_imagen(imagen1_negativa, "Imagen Negativa")

if __name__ == "__main__":
    main()