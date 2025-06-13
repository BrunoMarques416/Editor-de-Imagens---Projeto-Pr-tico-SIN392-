import cv2

def filtro_media(img):
    return cv2.blur(img, (5, 5))

def filtro_mediana(img):
    return cv2.medianBlur(img, 5)

def filtro_gaussiano(img):
    return cv2.GaussianBlur(img, (5, 5), 0)