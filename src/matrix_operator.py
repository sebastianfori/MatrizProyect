import numpy as np

class MatrixOperations:
    @staticmethod
    def check_reverse(matriz: np.ndarray):
        if matriz.shape[0] != matriz.shape[1]:
            return None  # No es una matriz cuadrada, no tiene inversa
        try:
            inversa = np.linalg.inv(matriz)
            return inversa
        except np.linalg.LinAlgError:
            return None  # No tiene inversa

    @staticmethod
    def multiply_by_scalar(matriz: np.ndarray, escalar: float):
        return np.clip(matriz * escalar, 0, 255).astype(np.uint8)


    @staticmethod
    def turn_image_x_axis(matriz: np.ndarray):
        return np.flipud(matriz)

    @staticmethod
    def calculate_negatve(matriz: np.ndarray):
        matriz_auxiliar = np.full_like(matriz, 255)
        return matriz_auxiliar - matriz