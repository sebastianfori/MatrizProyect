import cv2
import numpy as np
def show_image(imagen, titulo="Imagen"):
    cv2.imshow(titulo, imagen)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def save_image(imagen, ruta_salida):
    cv2.imwrite(ruta_salida, imagen)

def print_matrix(matriz: np.ndarray, precision: int = 3):
    # Usa un formato bonito para los números, controlando la precisión
    formatted = np.array2string(
        matriz, 
        formatter={'float_kind': lambda x: f"{x:.{precision}f}"},  # Formateo con precisión
        max_line_width=120  # Controla el ancho de la línea para que no se divida mucho
    )
    print(formatted)