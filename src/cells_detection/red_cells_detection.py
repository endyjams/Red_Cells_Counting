import matplotlib.pyplot as plt
from read_images import ReadImages
from HSV import remove_white_cells as rwc
import numpy as np
import cv2

def RedCellsDetection(img):
    # Função para trabalhar que trabalha no canal HSV (remoção das células brancas)
    remove_white_cells = rwc.RemoveWhiteCells(img)

    red_cells_img = img.copy()

    # Conversão de RGB para tons de cinza
    gray_img = cv2.cvtColor(remove_white_cells, cv2.COLOR_BGR2GRAY)

    # Melhora de contraste com a aplicação de CLAHE
    clahe = cv2.createCLAHE(2.0, (8,8))

    clahe_img = clahe.apply(gray_img)

    # Aplicando filtro gaussiano para remoção de ruídos

    blurry_img = cv2.GaussianBlur(clahe_img, (5, 5), 0)

    # Aplicando threshold para binarização da imagem
    binary_img = cv2.adaptiveThreshold(blurry_img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 2)

    # Aplicando erosão na imagem para preenchimento dos buracos das células
    kernel = np.ones((4,4),np.uint8)
    eroding_img = cv2.erode(binary_img, kernel, 3)

    # Aplicação de Fechamento para remoção de pontos (ruídos)
    closing_img = cv2.morphologyEx(eroding_img, cv2.MORPH_CLOSE, kernel)

    # Usando o inverso da imagem para detecção das células
    inverse_img = 255-closing_img
    
    # Detecção dos círculos da imagem com CHT
    contours, hierarchy = cv2.findContours(inverse_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    red_cells = []

    red_cells_count = 0

    for c in contours:
        (x, y), r = cv2.minEnclosingCircle(c)

        x1 = x-r
        x2 = x+r
        y1 = y-r
        y2 = y+r

        if r >= 19 and r <= 160:
            cv2.rectangle(red_cells_img, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
            red_cells_count += 1

    fig, ax = plt.subplots(nrows=3, ncols=3, figsize=(10,7))
    fig.subplots_adjust(hspace= 0.5, wspace= 0.5)

    ax[0][0].imshow(img)
    ax[0][0].set_title('Original')

    ax[0][1].imshow(remove_white_cells)
    ax[0][1].set_title('HSV')

    ax[0][2].imshow(gray_img, cmap='gray')
    ax[0][2].set_title('Gray')

    ax[1][0].imshow(blurry_img, cmap='gray')
    ax[1][0].set_title('Clahe')

    ax[1][1].imshow(blurry_img, cmap='gray')
    ax[1][1].set_title('Gaussian Blur')

    ax[1][2].imshow(binary_img, cmap='gray')
    ax[1][2].set_title('Binary')

    ax[2][0].imshow(closing_img, cmap='gray')
    ax[2][0].set_title('Eroding then Closing')

    ax[2][1].imshow(inverse_img, cmap='gray')
    ax[2][1].set_title('Inverse')

    ax[2][2].imshow(red_cells_img)
    ax[2][2].set_title('Red Cells: ' + str(red_cells_count))
    

    plt.show()