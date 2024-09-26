import numpy as np

class OperacionesMatrices:
    @staticmethod
    def verificar_inversa(matriz: np.ndarray):
        # Verifica si la matriz tiene inversa
        if matriz.shape[0] != matriz.shape[1]:
            return None  # No es una matriz cuadrada, no tiene inversa
        try:
            inversa = np.linalg.inv(matriz)
            return inversa
        except np.linalg.LinAlgError:
            return None  # No tiene inversa

    @staticmethod
    def multiplicar_por_escalar(matriz: np.ndarray, escalar: float):
        # Multiplicamos la imagen (matriz) por un escalar
        return np.clip(matriz * escalar, 0, 255).astype(np.uint8)


    @staticmethod
    def voltear_imagen_eje_x(matriz: np.ndarray):
        # Volteamos la imagen alrededor del eje X invirtiendo el orden de las filas
        return np.flipud(matriz)

    @staticmethod
    def calcular_negativo(matriz: np.ndarray):
        # Calcula el negativo de la imagen
        matriz_auxiliar = np.full_like(matriz, 255)
        return matriz_auxiliar - matriz