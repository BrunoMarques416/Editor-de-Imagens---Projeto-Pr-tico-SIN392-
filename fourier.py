import numpy as np
import cv2
import matplotlib.pyplot as plt

def mostrar_espectro(img):
    if img is None:
        return

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) if len(img.shape) == 3 else img
    f = np.fft.fft2(gray)
    fshift = np.fft.fftshift(f)
    magnitude_spectrum = 20 * np.log(np.abs(fshift) + 1)

    plt.figure("Espectro de Fourier")
    plt.title("Magnitude do Espectro")
    plt.imshow(magnitude_spectrum, cmap='gray')
    plt.colorbar()
    plt.show()