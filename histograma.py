import cv2
import matplotlib.pyplot as plt

def exibir_histograma(img):
    if img is None:
        return
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) if len(img.shape) == 3 else img
    hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
    plt.figure("Histograma")
    plt.title("Histograma de Intensidade")
    plt.xlabel("Intensidade")
    plt.ylabel("Frequência")
    plt.plot(hist)
    plt.xlim([0, 256])
    plt.grid()
    plt.show()