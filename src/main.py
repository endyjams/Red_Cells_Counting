import matplotlib.pyplot as plt
from read_images import ReadImages
from cells_detection import white_cells_detection as wcd
from cells_detection import red_cells_detection as rcd
import numpy as np
import cv2

def main():

    # Função para leitura das imagens
    images_list = ReadImages("archive/images")

    img = images_list[0]

    rcd.RedCellsDetection(img)

if __name__ == '__main__':
    main()