import cv2
import numpy as np

def filtro_media(img):
    return cv2.blur(img, (5, 5))

def filtro_mediana(img):
    return cv2.medianBlur(img, 5)

def filtro_gaussiano(img):
    return cv2.GaussianBlur(img, (5, 5), 0)

def filtro_maximo(img, ksize=3):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) if len(img.shape) == 3 else img
    kernel = np.ones((ksize, ksize), np.uint8)
    return cv2.dilate(gray, kernel)

def filtro_minimo(img, ksize=3):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) if len(img.shape) == 3 else img
    kernel = np.ones((ksize, ksize), np.uint8)
    return cv2.erode(gray, kernel)
