import matplotlib.pyplot as plt
from read_images import ReadImages
from HSV import remove_white_cells as rwc
import numpy as np
import cv2

def main():

    # Função para leitura das imagens
    images_list = ReadImages("archive/images")

    first_img = images_list[0]

    # Função para trabalhar que trabalha no canal HSV (remoção das células brancas)
    remove_white_cells = rwc.RemoveWhiteCells(first_img)

    cht_img = first_img.copy()

    # Conversão de RGB para tons de cinza
    gray_img = cv2.cvtColor(remove_white_cells, cv2.COLOR_BGR2GRAY)

    # Melhora de contraste com a aplicação de CLAHE
    clahe = cv2.createCLAHE(2.0, (8,8))

    gray_img = clahe.apply(gray_img)

    # Aplicando filtro gaussiano para remoção de ruídos

    blurry_img = cv2.GaussianBlur(gray_img, (5, 5), 0)

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
    cht = cv2.HoughCircles(
        inverse_img, 
        cv2.HOUGH_GRADIENT, 
        1,
        20,
        param1=50, 
        param2=30, 
        minRadius=0, 
        maxRadius=0
    )

    cht = np.uint8(np.around(cht))

    red_cells = 0

    # Passeando pelas coordenadas dos círculos, apenas preservando os que tem raio >= 20 && raio <= 36
    for i in cht[0,:]:
        x = i[0]
        y = i[1]
        r = i[2]

        if r >= 18 and r <= 38:
            cv2.circle(cht_img, (x, y), r, (0, 255, 0), 2)
            red_cells += 1

        print(r)

    fig, ax = plt.subplots(nrows=3, ncols=3, figsize=(10,7))
    fig.subplots_adjust(hspace= 0.5, wspace= 0.5)

    ax[0][0].imshow(first_img)
    ax[0][0].set_title('Original')

    ax[0][1].imshow(remove_white_cells)
    ax[0][1].set_title('HSV')

    ax[0][2].imshow(gray_img, cmap='gray')
    ax[0][2].set_title('Gray')

    ax[1][0].imshow(blurry_img, cmap='gray')
    ax[1][0].set_title('Gaussian Blur')

    ax[1][1].imshow(binary_img, cmap='gray')
    ax[1][1].set_title('Binary')

    ax[1][2].imshow(closing_img, cmap='gray')
    ax[1][2].set_title('Closing')

    ax[2][0].imshow(opening_img, cmap='gray')
    ax[2][0].set_title('Opening')

    ax[2][1].imshow(cht_img)
    ax[2][1].set_title('CHT => Circles: ' + str(red_cells))
    

    plt.show()


if __name__ == '__main__':
    main()