
import cv2
import numpy as np

class ProcesadorImagen:
    def __init__(self, ruta_img: str):
        self.imagen = cv2.imread(ruta_img)
        if self.imagen is None:
            raise ValueError(f"No se pudo cargar la imagen desde {ruta_img}")
        self.altura, self.ancho, _ = self.imagen.shape

    def recortar(self, x_inicial: int, x_final: int, y_inicial: int, y_final: int):
        imagen_crop = self.imagen[y_inicial:y_final, x_inicial:x_final]
        return imagen_crop

    def mostrar(self, titulo="Imagen"):
        cv2.imshow(titulo, self.imagen)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def obtener_tamanio(self):
        return self.imagen.shape

    def convertir_a_grises(self):
        return cv2.cvtColor(self.imagen, cv2.COLOR_BGR2GRAY)

    def mostrar_como_matriz(self):
        return np.array(self.imagen)

    def transponer_imagen(self):
        return np.transpose(self.imagen, (1, 0, 2))

    def ajustar_contraste(self, alfa: float):
        # Aseguramos que los valores se mantengan entre 0 y 255
        imagen_ajustada = np.clip(self.imagen * alfa, 0, 255).astype(np.uint8)
        return imagen_ajustada

    def calcular_negativo(self):
        matriz_auxiliar = np.full_like(self.imagen, 255)
        imagen_negativa = matriz_auxiliar - self.imagen
        return imagen_negativa
