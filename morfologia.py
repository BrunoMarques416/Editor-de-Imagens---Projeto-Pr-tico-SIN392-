import cv2
import numpy as np

def aplicar_erosao(img, kernel_size=3, iterations=1):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) if len(img.shape) == 3 else img
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    erodida = cv2.erode(gray, kernel, iterations=iterations)
    return erodida

def aplicar_dilatacao(img, kernel_size=3, iterations=1):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) if len(img.shape) == 3 else img
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    dilatada = cv2.dilate(gray, kernel, iterations=iterations)
    return dilatada