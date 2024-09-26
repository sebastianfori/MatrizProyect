import cv2

def mostrar_imagen(imagen, titulo="Imagen"):
    cv2.imshow(titulo, imagen)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def guardar_imagen(imagen, ruta_salida):
    cv2.imwrite(ruta_salida, imagen)