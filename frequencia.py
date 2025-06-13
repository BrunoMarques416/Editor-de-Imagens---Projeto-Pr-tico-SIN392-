import numpy as np
import cv2

def filtro_freq_passa_baixa(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) if len(img.shape) == 3 else img
    f = np.fft.fft2(gray)
    fshift = np.fft.fftshift(f)
    rows, cols = gray.shape
    crow, ccol = rows//2, cols//2
    mask = np.zeros((rows, cols), np.uint8)
    mask[crow-30:crow+30, ccol-30:ccol+30] = 1
    fshift = fshift * mask
    img_back = np.fft.ifft2(np.fft.ifftshift(fshift))
    return np.abs(img_back).astype(np.uint8)

def filtro_freq_passa_alta(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) if len(img.shape) == 3 else img
    f = np.fft.fft2(gray)
    fshift = np.fft.fftshift(f)
    rows, cols = gray.shape
    crow, ccol = rows//2, cols//2
    mask = np.ones((rows, cols), np.uint8)
    mask[crow-30:crow+30, ccol-30:ccol+30] = 0
    fshift = fshift * mask
    img_back = np.fft.ifft2(np.fft.ifftshift(fshift))
    return np.abs(img_back).astype(np.uint8)