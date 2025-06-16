import sys
import cv2
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QFileDialog, QAction,
    QMessageBox, QWidget, QVBoxLayout, QHBoxLayout
)
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt

from histograma import exibir_histograma
from intensidade import alargamento_contraste, equalizacao_histograma
from passa_baixa import filtro_media, filtro_mediana, filtro_gaussiano
from passa_alta import filtro_laplaciano, filtro_sobel
from frequencia import filtro_freq_passa_baixa, filtro_freq_passa_alta
from fourier import mostrar_espectro
from morfologia import aplicar_erosao, aplicar_dilatacao
from segmentacao import segmentacao_otsu

class ImageEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Editor de Imagens - PyQt5")
        self.imagem_original = None
        self.imagem_processada = None

        self.img_label = QLabel("Imagem Original")
        self.result_label = QLabel("Imagem Processada")
        self.img_label.setAlignment(Qt.AlignCenter)
        self.result_label.setAlignment(Qt.AlignCenter)

        layout = QHBoxLayout()
        layout.addWidget(self.img_label)
        layout.addWidget(self.result_label)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.criar_menu()

    def criar_menu(self):
        menubar = self.menuBar()

        menu_arquivo = menubar.addMenu("Arquivo")
        abrir = QAction("Abrir Imagem", self)
        abrir.triggered.connect(self.carregar_imagem)
        salvar = QAction("Salvar Imagem Processada", self)
        salvar.triggered.connect(self.salvar_imagem)
        restaurar = QAction("Restaurar Original", self)
        restaurar.triggered.connect(self.restaurar_imagem)

        menu_arquivo.addAction(abrir)
        menu_arquivo.addAction(salvar)
        menu_arquivo.addAction(restaurar)

        menu_op = menubar.addMenu("Operações")
        menu_op.addAction("Histograma", lambda: exibir_histograma(self.imagem_processada if self.imagem_processada is not None else self.imagem_original))
        menu_op.addAction("Alargamento de Contraste", lambda: self.aplicar_processo(alargamento_contraste))
        menu_op.addAction("Equalização de Histograma", lambda: self.aplicar_processo(equalizacao_histograma))

        menu_passa_baixa = menu_op.addMenu("Filtros Passa-Baixa")
        menu_passa_baixa.addAction("Média", lambda: self.aplicar_processo(filtro_media))
        menu_passa_baixa.addAction("Mediana", lambda: self.aplicar_processo(filtro_mediana))
        menu_passa_baixa.addAction("Gaussiano", lambda: self.aplicar_processo(filtro_gaussiano))

        menu_passa_alta = menu_op.addMenu("Filtros Passa-Alta")
        menu_passa_alta.addAction("Sobel", lambda: self.aplicar_processo(filtro_sobel))
        menu_passa_alta.addAction("Laplaciano", lambda: self.aplicar_processo(filtro_laplaciano))
        menu_passa_alta.addAction("Roberts", lambda: self.aplicar_processo(filtro_roberts))
        menu_passa_alta.addAction("Prewitt", lambda: self.aplicar_processo(filtro_prewitt))

        menu_op.addAction("Filtro Freq. Baixa", lambda: self.aplicar_processo(filtro_freq_passa_baixa))
        menu_op.addAction("Filtro Freq. Alta", lambda: self.aplicar_processo(filtro_freq_passa_alta))
        menu_op.addAction("Espectro de Fourier", lambda: mostrar_espectro(self.imagem_processada if self.imagem_processada is not None else self.imagem_original))
        menu_op.addAction("Erosão", lambda: self.aplicar_processo(aplicar_erosao))
        menu_op.addAction("Dilatação", lambda: self.aplicar_processo(aplicar_dilatacao))
        menu_op.addAction("Segmentação Otsu", lambda: self.aplicar_processo(segmentacao_otsu))

    def carregar_imagem(self):
        caminho, _ = QFileDialog.getOpenFileName(self, 'Abrir imagem', '', 'Imagens (*.png *.jpg *.bmp)')
        if caminho:
            self.imagem_original = cv2.imread(caminho)
            self.imagem_processada = None
            self.mostrar_imagem(self.imagem_original, self.img_label)
            self.result_label.clear()

    def salvar_imagem(self):
        if self.imagem_processada is None:
            QMessageBox.warning(self, "Erro", "Nenhuma imagem processada para salvar.")
            return
        caminho, _ = QFileDialog.getSaveFileName(self, "Salvar imagem", "", "Imagens (*.png *.jpg *.bmp)")
        if caminho:
            cv2.imwrite(caminho, self.imagem_processada)
            QMessageBox.information(self, "Sucesso", "Imagem salva com sucesso!")

    def restaurar_imagem(self):
        if self.imagem_original is not None:
            self.imagem_processada = None
            self.mostrar_imagem(self.imagem_original, self.result_label)

    def mostrar_imagem(self, img, label):
        if len(img.shape) == 2:
            qimg = QImage(img.data, img.shape[1], img.shape[0], img.strides[0], QImage.Format_Grayscale8)
        else:
            rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            qimg = QImage(rgb.data, rgb.shape[1], rgb.shape[0], rgb.strides[0], QImage.Format_RGB888)
        label.setPixmap(QPixmap.fromImage(qimg).scaled(300, 300, Qt.KeepAspectRatio))

    def aplicar_processo(self, funcao):
        if self.imagem_original is None:
            QMessageBox.warning(self, "Erro", "Nenhuma imagem carregada.")
            return
        base = self.imagem_processada if self.imagem_processada is not None else self.imagem_original
        self.imagem_processada = funcao(base)
        self.mostrar_imagem(self.imagem_processada, self.result_label)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    editor = ImageEditor()
    editor.show()
    sys.exit(app.exec_())
