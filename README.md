# Editor de Imagens - Projeto Prático (SIN392)

Este projeto é um editor de imagens interativo desenvolvido em Python com interface gráfica em PyQt5. Ele foi criado como parte da disciplina **SIN392 - Introdução ao Processamento Digital de Imagens** na Universidade Federal de Viçosa - Campus Rio Paranaíba.

##  Funcionalidades

- Carregamento e visualização de imagens
- Cálculo e exibição do histograma
- Transformações de intensidade:
  - Equalização de histograma
  - Alargamento de contraste
- Filtros espaciais:
  - Filtros passa-baixa: média, mediana, gaussiano
  - Filtros passa-alta: Laplaciano, Sobel
- Filtros no domínio da frequência (Fourier)
- Visualização do espectro de Fourier
- Operações morfológicas:
  - Erosão
  - Dilatação
- Segmentação:
  - Método de Otsu
- Salvar imagem processada
- Aplicação de filtros encadeados
- Troca de imagem em tempo de execução
- Interface por menu com PyQt5

## 📁 Estrutura do Projeto

```
image_editor/
├── main.py
├── histograma.py
├── intensidade.py
├── passa_baixa.py
├── passa_alta.py
├── frequencia.py
├── fourier.py
├── morfologia.py
├── segmentacao.py
```

## 🚀 Como Executar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/image-editor-sin392.git
cd image-editor-sin392/image_editor
```

### 2. Instale as dependências

Certifique-se de estar em um ambiente com Python 3.7+:

```bash
pip install opencv-python PyQt5 matplotlib numpy
```

### 3. Execute o programa

```bash
python main.py
```

## 🖼️ Formatos Suportados

- PNG
- JPG
- BMP

## 📌 Observações

- Imagens RGB são convertidas automaticamente para escala de cinza quando necessário.
- Filtros podem ser aplicados em sequência.
- Recomenda-se usar imagens de tamanho moderado para melhor desempenho.

## 📚 Licença
---
Desenvolvido para a disciplina de Processamento Digital de Imagens.
