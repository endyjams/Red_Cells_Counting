import matplotlib.pyplot as plt
from read_images import ReadImages
from HSV import remove_white_cells as rwc
import numpy as np
from cells_detection import red_cells_detection as rcd
import cv2

def main():

    # Função para leitura das imagens
    images_list = ReadImages("archive/images")

    img = images_list[0]

    rcd.RedCellsDetection(img)

if __name__ == '__main__':
    main()