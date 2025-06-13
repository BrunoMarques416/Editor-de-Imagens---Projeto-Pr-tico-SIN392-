import cv2
import numpy as np
from scipy import ndimage

def filtro_laplaciano(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) if len(img.shape) == 3 else img
    lap = cv2.Laplacian(gray, cv2.CV_64F)
    lap = np.absolute(lap)
    lap = np.clip(lap, 0, 255)
    return lap.astype(np.uint8)

def filtro_roberts(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) if len(img.shape) == 3 else img
    kernel_x = np.array([[1, 0], [0, -1]], dtype=np.float32)
    kernel_y = np.array([[0, 1], [-1, 0]], dtype=np.float32)
    img_x = ndimage.convolve(gray, kernel_x)
    img_y = ndimage.convolve(gray, kernel_y)
    result = np.sqrt(img_x**2 + img_y**2)
    result = np.clip(result, 0, 255)
    return result.astype(np.uint8)

def filtro_prewitt(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) if len(img.shape) == 3 else img
    kernel_x = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]], dtype=np.float32)
    kernel_y = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]], dtype=np.float32)
    img_x = ndimage.convolve(gray, kernel_x)
    img_y = ndimage.convolve(gray, kernel_y)
    result = np.sqrt(img_x**2 + img_y**2)
    result = np.clip(result, 0, 255)
    return result.astype(np.uint8)

def filtro_sobel(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) if len(img.shape) == 3 else img
    img_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    img_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    sobel = np.hypot(img_x, img_y)
    sobel = np.clip(sobel, 0, 255)
    return sobel.astype(np.uint8)
